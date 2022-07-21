from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea


app = Flask(__name__) #En app se encuentra nuestro servidor web de Flask
@app.route("/")
def home():
    todas_las_tareas= db.session.query(Tarea).all() #14quiero enviar la variable todas_las_tareas al html a la parte de card body.

    return render_template('index.html',lista_de_tareas=todas_las_tareas) #14.1 invenvtamos el nombre de una variable y le asignamos la variable todas_las_tareas
                                                                            #ahora la variable (lista_de_tareas) esta accesible desde el html
@app.route("/editar/<id>",methods=['GET','POST'])
def editar(id):
    tarea=db.session.query(Tarea).get(id)
    print(tarea.fecha)
    return render_template("editar_tarea.html",tarea=tarea)

@app.route('/modificar/<id>', methods=['POST','GET'])
def modificar(id):
    item=db.session.query(Tarea).get(id)

    if len(item.contenido)>0:
        item.contenido=request.form['contenido']
    if len(item.categoria)>0:
        item.categoria=request.form['categoria']
    item.fecha=request.form['fecha']

    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))




@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido'], hecha=False,
                  categoria=request.form['categoria'], fecha=request.form['fecha']) #request.form busca en el formulario que tenemos la variable contenido-tarea, el input que tenemos en nuestro formulario
    db.session.add(tarea) #añade este objeto tarea a la base de datos
    db.session.commit()     #guardamos el objeto en la base de datos
    db.session.close()
    return redirect(url_for("home")) #redireccionar a donde apunta url_for en nuestro caso "home" o el nombre de una funcion que hayamos creado
        #con este redirect pdemos movernoes entre diferentes partes de una web.


@app.route('/eliminar-tarea/<id>') #si le ponemos los simbolos <> app.route se espera una variable y por lo tanto ahora si ejecutara la funcion eliminar
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=id).delete()
    db.session.commit()     #guardamos el objeto en la base de datos
    db.session.close()
    return redirect(url_for("home")) #redireccionar a donde apunta url_for en nuestro caso "home" o el nombre de una funcion que hayamos creado
        #con este redirect pdemos movernoes entre diferentes partes de una web.

@app.route('/tarea-hecha/<id>') #si le ponemos los simbolos <> app.route se espera una variable y por lo tanto ahora si ejecutara la funcion eliminar
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=id).first()
    tarea.hecha = not (tarea.hecha)
    db.session.commit()     #guardamos el objeto en la base de datos
    db.session.close()
    return redirect(url_for("home")) #redireccionar a donde apunta url_for en nuestro caso "home" o el nombre de una funcion que hayamos creado
        #con este redirect pdemos movernoes entre diferentes partes de una web.


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)     # El debug True hace que cada vez que reiniciemos el servidor o modifiquemos codigo,
                            #el servidor de flask se reinicie solo

