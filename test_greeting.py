# test_greeting.py
from greeting import greeting

def test_greeting():
  """
  Memverifikasi bahwa fungsi greeting bekerja sesuai harapan.
  """
  # KESALAHAN SEBELUMNYA: assert greeting(“Polibest") ... 
  # PERBAIKAN: Menggunakan tanda kutip lurus " " yang valid di Python.
  assert greeting("Polibest") == "Hello Polibest, welcome to DevSecOps!"

