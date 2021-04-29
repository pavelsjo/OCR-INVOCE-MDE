# Extractor de Metadatos de Facturas OCR

El siguiente código permite extraer los metadatos de una `factura escaneada` y almacenada en formato `.pdf`, por ejemplo:

<img src="./raw/factura_001.png" alt="Ejemplo Factura" title="Ejemplo Factura" width="400" height="500" />

|INVOICE|DATE|TOTAL DUE|
|--|--|--|
1989|09/12/2005|1.596.097

La ejecución se inicia con un pre-procesamiento con `ImageMagick`, luego, se convierten los caracteres a texto plano con `pytesseract` y se utilizan `regex` para extraer los metadatos; finalmente el resultado queda en formato json.

Para utilizarlo se deben instalar las siguientes dependencias:

## Instalar ImageMagick en Red Hat 4.8.5-16.0.3

```Shel
sudo yum -y update 
sudo yum -y install ImageMagick-devel
```

Para la instalación en otras distribuciones, por favor revisa la [documentación oficial](https://docs.wand-py.org/en/latest/guide/install.html).

## Instalar Tesseract en Red Hat RHEL 7 

```Shell
sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo subscription-manager repos --enable "rhel-*-optional-rpms" --enable "rhel-*-extras-rpms"
sudo yum -y update
sudo yum -y install snapd
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo /usr/bin/yum --enablerepo epel-testing -y install tesseract.x86_64 tesseract-langpack-fra.noarch
```

## Version Alternativa

```Shell
sudo yum install install poppler-utils
```

## Librerías python

Este código fué probado con `python3.6` y requiere instalar los siguientes paquetes:

```Shell
pip install -r requeriments.txt
```

## Referencias

- [Enable snaps on Red Hat Enterprise Linux and install tesseract](https://snapcraft.io/install/tesseract/rhel)
- [Installing Tesseract-OCR on CentOS 6](https://stackoverflow.com/questions/23792373/installing-tesseract-ocr-on-centos-6)
- [Poppler in path for pdf2image](https://stackoverflow.com/questions/53481088/poppler-in-path-for-pdf2image)
- [pdf2image-github](https://github.com/Belval/pdf2image)
- [pdf2image-pypi](https://pypi.org/project/pdf2image/)