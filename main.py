from functions import obtain as colect_data_from, decipher_message, cipher_message, cipher

alphabet, people, messages = colect_data_from('resources/datos_7.txt')

sender, receiver, msg = people['Benito'], people['Alicia'], messages[0]
message = decipher_message(receiver, msg, alphabet)
print(message)

sender, receiver, msg = people['Alicia'], people['Benito'], messages[1]
message = cipher_message(receiver, msg, alphabet)
print(message)