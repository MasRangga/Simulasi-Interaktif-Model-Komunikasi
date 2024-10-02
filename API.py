# Import Libraries
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Inisialisasi Flask
app = Flask(__name__)
CORS(app)


# Kelas CommunicationSystem
class CommunicationSystem:

    def __init__(self):
        self.database = {
            "halo":
            "Halo! Selamat datang! Ada yang bisa saya bantu?",
            "apa yang bisa kamu lakukan?":
            "Saya dapat memberikan informasi tentang musik metal dan merekomendasikan lagu-lagu terbaik!",
            "bagaimana cara menemukan musik baru?":
            "Anda dapat menjelajahi genre musik metal atau meminta rekomendasi berdasarkan artis favorit Anda."
        }

    def process_request(self, user_input):
        response = self.database.get(
            user_input.lower(), "Maaf, saya tidak mengerti pertanyaan Anda.")
        return response


# Inisialisasi Objek CommunicationSystem
communication_system = CommunicationSystem()


# Rute untuk menampilkan halaman chat (GET request)
@app.route('/', methods=['GET'])
def index():
    return render_template("ChatbotAI.html")


# Rute API untuk memproses chat (POST request)
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('user_input', '')
    print(f"User Input: {user_input}")
    response = communication_system.process_request(user_input)
    print(f"AI Response: {response}")
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=False, port=3000, host='0.0.0.0')
