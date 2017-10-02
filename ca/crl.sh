SHELL=/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/opt/ca

openssl ca -gencrl -config YOUR_CA_DIRECTORY/etc/signing-ca.conf -out YOUR_CA_DIRECTORY/crl/signing-ca.crl -passin pass:YOURPASS
cp /opt/ca/crl/signing-ca.crl /usr/share/nginx/html
