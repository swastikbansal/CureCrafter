import speech_recognition as sr
from googletrans import Translator



def takeCommandHindi(): 
		
	r = sr.Recognizer() 
	with sr.Microphone() as source: 
		
		print('Listening your problem') 
		r.pause_threshold = 0.7
		audio = r.listen(source) 
		try: 
			print("Recognizing that you spoke") 
			QueryH= r.recognize_google(audio, language='hi-In') 
			
			# for listening the command in hindi 
			print("the query is ='", QueryH, "'") 
		
		except Exception as e: 
			print(e) 
			print("Say that again sir") 
			return "None"
		return QueryH

def takeCommandEnglish(): 
		
	r = sr.Recognizer() 
	with sr.Microphone() as source: 
		
		print('Listening your problem') 
		r.pause_threshold = 0.7
		audio = r.listen(source) 
		try: 
			print("Recognizing that you spoke") 
			Query = r.recognize_google(audio, language='en') 
			
			# for listening the command in english 
			print("the query is ='", Query, "'") 
		
		except Exception as e: 
			print(e) 
			print("Say that again sir") 
			return "None"
		return Query 
print("Enter the language you want to speak")
print("For Hindi Press 0")
print("For English Press 1")
language=int(input("Enter The Number : "))
if(language==0):
	takeCommandHindi()
else:
	takeCommandEnglish()
HinToEng=takeCommandHindi()


translator=Translator()
translation=translator.translate(HinToEng,src="hi",dest="en")
text=translation.text
print (text)


#result=translate_to_english(HinToEng)
#print("Translated text in English :",result)