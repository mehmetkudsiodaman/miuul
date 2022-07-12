##########################################
# Virtual Environment - Package Management
##########################################

# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create -n summercamp(environment's name)

# Sanal ortamı environment dosyasından oluşturma:
# conda env create -f environment.yaml

# Sanal ortam silme:
# conda env remove -n summercamp(environment's name)

# Sanal ortamı aktif-deaktif etme:
# conda activate summercamp(environment's name)
# conda deactivate

# Ortam içindeki paketlerin listelenmesi:
# conda list

# Ortam içine paket yüklemek:
# conda install numpy

# Ortam içine belirli bir versiyona göre paket yüklemek:
# conda install numpy=1.20.1

# Ortam içine yüklenmiş paketi yükseltme:
# conda upgrade numpy

# Ortam içine yüklenmiş tüm paketleri yükseltme:
# conda upgrade -all

# Ortam içine birden fazla paket yüklemek:
# conda install numpy scipy pandas

# Ortamdan paket silmek:
# conda remove numpy

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install pandas

# Paket yükleme versiyona göre:
# pip install pandas==1.2.1

# Kütüphane-paket aktarımı:
# conda env export > environment.yaml


###############################################
# Atamalar ve Değişkenler (Assignments & Variables)
###############################################
a = 9
a

b = "hello ai era"
b

c = 10
a * c
a * 10
d = a - c

