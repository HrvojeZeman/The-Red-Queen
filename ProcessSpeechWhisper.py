import whisper
model = whisper.load_model("base")
result = model.transcribe("recorded_output.wav", language="en")
print(result["text"])