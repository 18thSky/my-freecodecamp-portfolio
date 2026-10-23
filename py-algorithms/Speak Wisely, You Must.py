def wise_speak(sentence):
    hold_punctuation = sentence[-1]
    rest_of_sentence = sentence[:-1]
    words = rest_of_sentence.split(" ")
    for index,pivot in enumerate(words):
        if pivot in ["have", "must", "are", "will", "can"]:
            split_index = index
            break
    front_half = words[:split_index+1]
    back_half = words[split_index +1:] 
    re_join_1 = " ".join(back_half)
    re_join_2 = " ".join(front_half)
    re_join_1 = re_join_1.capitalize()
    re_join_2 = re_join_2.lower()

    return f"{re_join_1}, {re_join_2}{hold_punctuation}"

wise_speak("You can do it!")
wise_speak("Do you think you will complete this?")
wise_speak("You must speak wisely.")
wise_speak("All your base are belong to us.")
wise_speak("You have much to learn.")