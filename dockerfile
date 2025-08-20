# Dockerfile for RHEL 9 ARM64
FROM httpd:alpine

# Remove default index
RUN rm /usr/local/apache2/htdocs/index.html

# Add your custom index.html
ADD ./index.html /usr/local/apache2/htdocs/index.html

# Set working directory (optional)
WORKDIR /usr/local/apache2/htdocs/

# Expose HTTP port
EXPOSE 80

# Start Apache server
CMD ["httpd", "-D", "FOREGROUND"]
