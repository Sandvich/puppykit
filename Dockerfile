FROM httpd:2.4-alpine

COPY ./ /usr/local/apache2/htdocs/
RUN mv /usr/local/apache2/htdocs/httpd.conf /usr/local/apache2/conf/httpd.conf &&\
    chown -R daemon:daemon /usr/local/apache2/ && chmod -R 777 /usr/local/apache2/
