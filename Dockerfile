FROM nlpbox/nlpbox-base:16.04
MAINTAINER Arne Neumann <nlpbox.programming@arne.cl>

RUN apt-get update -y && apt-get install -y make g++ flex

WORKDIR /opt
RUN git clone https://github.com/BLLIP/bllip-parser

WORKDIR /opt/bllip-parser
RUN make

ENTRYPOINT ["./parse.sh"]  
CMD ["/opt/bllip-parser/sample-text/sample-data.txt"]
