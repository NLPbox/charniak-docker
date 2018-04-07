FROM nlpbox/nlpbox-base:16.04
MAINTAINER Arne Neumann <nlpbox.programming@arne.cl>

RUN apt-get update -y && \
    apt-get install -y make g++ flex swig2.0 python-pip && \
    pip install pytest sh

WORKDIR /opt
RUN git clone https://github.com/BLLIP/bllip-parser

# To make the Charniak parser build process fully reproducible, we will
# build a specific commit (i.e. the most recent commit
# available on 2018-04-06).
WORKDIR /opt/bllip-parser
RUN git checkout -b 2018-04-06 f83be9f1453a47d5e5b9f9694da8d0950778fb99 && \
    make && python setup.py install

ADD test_charniak.py /opt/bllip-parser/

ENTRYPOINT ["./parse.sh"]  
CMD ["/opt/bllip-parser/sample-text/sample-data.txt"]
