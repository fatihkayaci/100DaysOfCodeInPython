try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["keyasdasdasd"])
except IndexError:
    file = open("a_file.txt", "w")
except KeyError as error_message:
    print(f"at arabası{error_message}")
else:
    print("it was write")
finally:
    file.close()
    print("it was closed")