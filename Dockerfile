RUN git clone https://github.com/pebasaraputa/sindupothabot.git /root/sindupothabot
WORKDIR /root/sindupothabot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
