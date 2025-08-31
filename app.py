from flask import Flask, jsonify, request, Response
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from models import Adv, db
import os, json
import time
from flask_migrate import Migrate

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://adv_user:adv_pass@postgres_db:5432/adv_db')

db.init_app(app)

migrate = Migrate(app, db)

def json_response(data, status=200):
    """Создает JSON ответ с правильной кодировкой UTF-8"""
    return Response(
        json.dumps(data, ensure_ascii=False),
        status=status,
        mimetype='application/json; charset=utf-8'
    )

@app.route('/test', methods=['GET'])
def test():
    response = {'message': 'Тестовое сообщение', 'status': 'OK'}
    
    return json_response(response), {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/')
def index():
    return 'Hello, World!'

class AdvView(MethodView):

    def post(self):
        try:
            data = request.json
            new_adv = Adv(title=data['title'], description=data['description'], owner=data['owner'])
            db.session.add(new_adv)
            db.session.commit()
            return json_response({'message': 'Объявление создано', 'id': new_adv.id, 'created_at': new_adv.created_at.isoformat()}), 201
        except Exception as e:
            db.session.rollback()
            return json_response({'error': 'Не удалось создать объявление', 'details': str(e)}, ensure_ascii=False), 500  

    def patch(self, adv_id):
        adv = Adv.query.get(adv_id)
        if not adv:
            return json_response({'error': 'Объявление не найдено'}, ensure_ascii=False), 404
        data = request.json
        if 'title' in data:
            adv.title = data['title']
        if 'description' in data:
            adv.description = data['description']
        if 'owner' in data:
            adv.owner = data['owner']
        db.session.commit()
        
        return json_response({'message': 'Объявление изменено'}, ensure_ascii=False), 200
    
    def get(self, adv_id=None):
        if adv_id is None:
            advs = Adv.query.all()

            for adv in advs:
                print(f"Retrieved from DB - Title: {adv.title}, Description: {adv.description}, Owner: {adv.owner}")

            response_data = [{'title': adv.title, 
                          'description': adv.description, 
                          'owner': adv.owner, 
                          'created_at': adv.created_at.isoformat()} for adv in advs]        
        
            return json_response(response_data), 200

        adv = Adv.query.get(adv_id)
        if not adv:
            return json_response({'error': 'Объявление не найдено'}), 404

        response_data = {
        'title': adv.title,
        'description': adv.description,
        'owner': adv.owner,
        'created_at': adv.created_at.isoformat()}    
    
        return json_response(response_data), 200 

    def delete(self, adv_id):
        adv = Adv.query.get(adv_id)
        if not adv:
            return json_response({'error': 'Объявление не найдено'}), 404
        db.session.delete(adv)
        db.session.commit()
        return '', 204    

app.add_url_rule('/adv', view_func=AdvView.as_view('adv_list'), methods=['POST', 'GET']) 
app.add_url_rule('/adv/<int:adv_id>', view_func=AdvView.as_view('adv_detal'), methods=['GET', 'PATCH', 'DELETE']) 

if __name__ == '__main__':

    with app.app_context():
        while True:
            try:
                db.create_all()
                print('Таблицы созданы успешно')
                break
            except Exception as e:
                print(f'Ошибка подключения к БД: {e}')
                time.sleep(5)
    
    app.run(host = '0.0.0.0', port = 5000, debug=True)


