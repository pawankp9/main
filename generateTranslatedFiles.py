import os

from readWordFile import read_word_file
from wordFileToExcelDataFrame import genWordContentToDataframe
from EnglishToLanguageTranslator import languageTranslator

language = 'spanish'
fileName = "/Users/pawan/Desktop/myPython/documentChatbot/langConvertor/dataSample/Navigating in Yammer & Using the Inbox in Yammer Web 2020.docx"

wordContent, file_name_without_extension = read_word_file(fileName)

dataFrameEnglish = genWordContentToDataframe(wordContent, file_name_without_extension)

progressStatus = languageTranslator(dataFrameEnglish, language, file_name_without_extension)
