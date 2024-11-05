from flask import Flask, render_template
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema, Int, List

app = Flask(__name__)

# Data wisata
wisata_data = [
    {"id": 1, "nama": "Candi Borobudur", "deskripsi": "Candi Buddha terbesar di dunia.", "gambar": "/static/borobudur.jpeg"},
    {"id": 2, "nama": "Raja Ampat", "deskripsi": "Keindahan alam bawah laut dan keanekaragaman hayati.", "gambar": "/static/rajaampat.jpeg"},
    {"id": 3, "nama": "Diamond Beach", "deskripsi": "Pantai di Pulau Bali, Nusa Penida.", "gambar": "/static/diamondbeach.jpeg"},
    {"id": 4, "nama": "Gunung Bromo", "deskripsi": "Gunung berapi aktif dengan pemandangan dramatis.", "gambar": "/static/gunungbromo.jpeg"},
]

# Definisikan skema GraphQL menggunakan graphene
class WisataType(ObjectType):
    id = Int()
    nama = String()
    deskripsi = String()
    gambar = String()

class Query(ObjectType):
    daftar_wisata = List(WisataType)

    def resolve_daftar_wisata(root, info):
        return wisata_data

schema = Schema(query=Query)

# Tambahkan rute untuk halaman HTML
@app.route("/")
def index():
    return render_template("index.html")

# Tambahkan rute untuk GraphQL
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(debug=True)
