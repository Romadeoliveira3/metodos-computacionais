from flask import Blueprint, session,render_template, request, redirect, url_for, flash
from config import MODELS_DIR
from aula import Aula
from lista_de_aulas import ListaDeAulas
from db import get_db
import sqlite3


main = Blueprint('main', __name__)

@main.route("/")
def home():
    db = get_db()
    aulas_db = db.execute('SELECT * FROM aulas').fetchall()
    return render_template("home.html", aulas=aulas_db)

@main.route("/add_aula", methods=["GET", "POST"])
def add_aula():
    if request.method == "GET":  # Corrigido aqui
        return render_template("add_aula.html")
    else:
        # nome = request.args.get("nome", type = str)
        nome = request.form.get('nome')
        carga_horaria = int(request.form["carga_horaria"])
        aulas_semana = int(request.form["aulas_semana"])
        
        # Criar uma nova instância da classe Aula
        aula = Aula(nome, carga_horaria, aulas_semana)

        # Conectar ao banco de dados
        db = get_db()

        # Inserir a nova aula no banco de dados
        db.execute('''
            INSERT INTO aulas (nome, carga_horaria, aulas_semana, semanas, total_aulas, aulas_faltadas)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (aula.nome, aula.carga_horaria, aula.aulas_semana, aula.semanas, aula.total_aulas, aula.aulas_faltadas)
        )

        # Salvar (commit) as alterações
        db.commit()

        # # Fechar a conexão com o banco de dados
        # db.close()

        return redirect(url_for("main.home"))

@main.route("/show_aulas", methods=["GET"])
def show_aulas():
    db = get_db()
    aulas_db = db.execute('SELECT * FROM aulas').fetchall()
    return render_template("show_aulas.html", aulas=aulas_db)


@main.route("/add_falta", methods=["GET","POST"])
def add_falta():
    db = get_db()
    cur = db.cursor()
    if request.method == "GET":
        nome = request.args.get('nome', default = None, type = str)
        if nome is not None:
            cur.execute("SELECT * FROM aulas WHERE nome = ?", (nome,))
            aula_data = cur.fetchone()
            print("Print antes do Aula_data", aula_data)
            if aula_data is not None:
                aula = Aula(*aula_data)
                faltas = aula.aulas_faltadas
                faltas_restantes = (aula.total_aulas * 0.25) - aula.aulas_faltadas
            else:
                faltas = 0
                faltas_restantes = 0
        else:
            faltas = 0
            faltas_restantes = 0
        aulas = cur.execute('SELECT * FROM aulas').fetchall()
        print("Print antes do render_template:",faltas, faltas_restantes)
        return render_template("add_falta.html", aulas=aulas, selected_nome=nome, faltas=faltas, faltas_restantes=faltas_restantes)
    else:
        nome = request.form['nome']
        cur.execute("SELECT * FROM aulas WHERE nome = ?", (nome,))
        aula_data = cur.fetchone()
        if aula_data is not None:
            aula = Aula(*aula_data)
            aula.adicionar_falta()
            cur.execute("""
                UPDATE aulas
                SET aulas_faltadas = ?
                WHERE nome = ?
            """, (aula.aulas_faltadas, aula.nome))
            db.commit()
        return redirect(url_for("main.home"))
