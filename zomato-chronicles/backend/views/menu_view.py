from flask import Blueprint
menu_bp=Blueprint('menu',__name__)
@menu_bp.route('/menu',methods=['GET'])
def get_menu():
    