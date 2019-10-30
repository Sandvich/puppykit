FROM nginx:mainline-alpine

COPY . /code
RUN ln -s /code/system/puppykit.conf /etc/nginx/conf.d/puppykit.conf && \
    rm /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]