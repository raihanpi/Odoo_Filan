FROM odoo:16

# if you have to install from pip and using Odoo >= 11.0
USER root
ENV PATH="/var/lib/odoo/.local/bin:${PATH}"
RUN pip3 install wheel
RUN pip3 install supabase
RUN pip3 install xlsxwriter
RUN pip3 install xlrd
RUN pip3 install rsa
RUN pip3 install pandas
RUN pip3 install python-whois
RUN pip3 install requests
RUN pip3 install midtransclient
RUN pip3 install oauthlib pyjwt gcloud google-cloud-storage bs4 pydrive instagram_private_api midtransclient
RUN pip3 install libsass
RUN pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip3 install pydrive
COPY custom_modules/cnt_pm/key/client_secrets.json /client_secrets.json
COPY custom_modules/cnt_pm/key/mycreds.txt /mycreds.txt
RUN chmod 777 /mycreds.txt /client_secrets.json
USER odoo