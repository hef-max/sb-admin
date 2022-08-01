from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/admin')
def admin():
	title = "Dashboard"
	return render_template('admin.html', title=title)

@app.route('/dosen')
def dosen():
	title = "Daftar Dosen"
	return render_template('dosen.html', title=title)

@app.route('/mahasiswa')
def mahasiswa():
	title = "Data Mahasiswa"
	return render_template('mahasiswa.html', title=title)

@app.route('/pegawai')
def pegawai():
	title = "Daftar Pegawai"
	return render_template('pegawai.html', title=title)

@app.route('/jadwal')
def jadwal():
	title = "Jadwal Kuliah"
	return render_template('jadwal.html', title=title)

@app.route('/nilai')
def nilai():
	title = "Nilai Mahasiswa"
	return render_template('nilai.html', title=title)

if __name__=='__main__':
	app.run(debug=True)