from subprocess import Popen

    
def preprocess_stream(stream):
    for chunk in stream:
        yield chunk["message"]["content"]