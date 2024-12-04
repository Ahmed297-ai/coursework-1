def hide_message(image_path, message):
    
    with open(image_path, 'rb') as image_file:
        image_data = bytearray(image_file.read())

 
    output_file = "output.bmp"

    message += "###"
    binary_message = "".join(f"{ord(char):08b}" for char in message)

   
    if len(binary_message) > (len(image_data) - 54):
        raise ValueError("The message is too large to fit in this image.")

    
    counter = 0
    for i in range(54, 54 + len(binary_message)):  # Start at byte 54 to avoid headers
        # Set the least significant bit to the corresponding bit in the message
        image_data[i] = (image_data[i] & 0b11111110) | int(binary_message[counter])
        counter += 1

    # Save the modified image
    with open(output_file, 'wb') as output:
        output.write(image_data)

    print(f"Message hidden successfully in {output_file}.")
    return output_file


def decode(image_path):
    # Open the image file containing the hidden message
    with open(image_path, "rb") as image_file:
        image_data = bytearray(image_file.read())

    # Extract the LSBs starting from the 54th byte
    binary_message = "".join(str(image_data[i] & 1) for i in range(54, len(image_data)))

    
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8:
            break  
        message += chr(int(byte, 2))

    delimiter = message.find("###")
    if delimiter != -1:
        return message[:delimiter]
    return "No hidden message found."


def choose_action():
    
    action = input("Would you like to encode or decode a message? (Enter 'encode' or 'decode') ").strip().lower()

    if action == 'encode':
        message = input("Enter the message to hide:\n")
        image_path = input("Enter the path of the image to hide the message in (e.g., input.bmp):\n")
        hide_message(image_path, message)
    elif action == 'decode':
        image_path = input("Enter the path of the image to decode the message from (e.g., output.bmp):\n")
        print("Decoded message:", decode(image_path))
    else:
        print("Invalid option. Please enter 'encode' or 'decode'.")
        choose_action()  


choose_action()