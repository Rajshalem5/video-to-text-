import assemblyai as aai
import textwrap

aai.settings.api_key = "cad1ff3f29f54097b468031d6387debf"
transcriber = aai.Transcriber()

# Replace "news.mp4" with the correct local file path
transcript = transcriber.transcribe("C:\\Users\\vajra\\Downloads\\1min.mp4")

if transcript and transcript.text:
    transcript_lines = transcript.text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=50) for line in transcript_lines]
    wrapped_trans = '\n'.join(wrapped_lines)
    print(wrapped_trans)
else:
    print("Transcription failed or returned empty.")
