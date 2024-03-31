FROM python
WORKDIR /chatbot
COPY . /chatbot
RUN pip install update
RUN pip install -r requirements.txt

ENV TLG_ACCESS_TOKEN=6991233385:AAESeyTXbe_59xrrh6OJmBXcLdXtrdHGOvg
ENV BASICURL=https://chatgpt.hkbu.edu.hk/general/rest
ENV MODELNAME=gpt-4-turbo
ENV APIVERSION=2023-12-01-preview
ENV ACCESS_TOKEN=6d3db42d-ce46-4c6d-8081-6062509e96ad

CMD python chatbot.py