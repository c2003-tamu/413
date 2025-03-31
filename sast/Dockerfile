FROM btnguyen2k/codeql-container

WORKDIR /opt/src

COPY . /opt/src

VOLUME ["/opt/results"]

CMD ["security", "--override", "--language=python", "--output=csv"]
