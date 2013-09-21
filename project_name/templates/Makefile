BASE_HTML = base.html
NOT_FOUND = notfound.html
INTERNAL_SERVER_ERROR = internal_server_error.html

all: 404.html 500.html

404.html: $(NOT_FOUND) $(BASE_HTML)
	../../manage.py render $(NOT_FOUND) 404.html;\
	sed -i "/^[[:blank:]]*$$/d" 404.html

500.html: $(INTERNAL_SERVER_ERROR) $(BASE_HTML)
	../../manage.py render $(INTERNAL_SERVER_ERROR) 500.html;\
	sed -i "/^[[:blank:]]*$$/d" 500.html

clean:
	-rm -rf 404.html 500.html
