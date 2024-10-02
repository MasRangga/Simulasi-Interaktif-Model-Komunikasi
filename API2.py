# Import modul-modul yang dibutuhkan
from flask import Flask, Response, request
import threading
import queue
import time
from flask_cors import CORS

# Inisialisasi Flask
app = Flask(__name__)
CORS(app)

# Inisialisasi antrian Log
log_queue = queue.Queue()  # Antrian untuk menyimpan log dari produsen
stop_event = threading.Event()  # Event untuk menghentikan thread


# Fungsi produsen
def producer(q):
    for i in range(1, 11):  # Menghasilkan angka dari 1 hingga 10
        if stop_event.is_set():  # Cek apakah thread harus berhenti
            break
        data = f"Saya ingin jual minyak: {i} ton"
        q.put(data)
        log_queue.put(data)  # Menyimpan log ke log_queue
        time.sleep(1)


# Rute API untuk memulai thread
@app.route('/', methods=['POST'])
def start_threads():
    global prod_thread
    stop_event.clear()  # Reset event untuk memulai thread
    q = queue.Queue()
    prod_thread = threading.Thread(target=producer, args=(q, ))

    prod_thread.start()

    return {"message": "Proses telah dimulai."}


# Rute API untuk menghentikan thread
@app.route('/stop', methods=['POST'])
def stop_threads():
    stop_event.set()  # Set event untuk menghentikan thread
    prod_thread.join()  # Tunggu hingga produsen selesai
    return {"message": "Proses telah dihentikan."}


# Rute API untuk menampilkan hasil dari produsen
@app.route('/result')
def stream_result():

    def generate():
        while True:
            if not log_queue.empty():
                log = log_queue.get()
                yield f"data: {log}\n\n"
            else:
                time.sleep(1)

    return Response(generate(), mimetype="text/event-stream")


# Rute API untuk konsumen kedua
@app.route('/consumer', methods=['GET'])
def stream_consumer():

    def generate():
        while True:
            if not log_queue.empty():
                log = log_queue.get()
                yield f"data: {log} (Dari Konsumen)\n\n"
            else:
                time.sleep(1)

    return Response(generate(), mimetype="text/event-stream")


# Jalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=False, port=4000, host="0.0.0.0")
