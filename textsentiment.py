from textblob import TextBlob

text = '''
Ram is sad.
'''

print(text)
analysis = TextBlob(text)
print(analysis.sentiment)

