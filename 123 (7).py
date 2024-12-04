# def hide_message(image_path, message):
    
#     with open(image_path, 'rb') as image_file:
#         image_data = bytearray(image_file.read())

 
#     output_file = "output.bmp"

#     message += "###"
#     binary_message = "".join(f"{ord(char):08b}" for char in message)

   
#     if len(binary_message) > (len(image_data) - 54):
#         raise ValueError("The message is too large to fit in this image.")

    
#     counter = 0
#     for i in range(54, 54 + len(binary_message)):  # Start at byte 54 to avoid headers
#         # Set the least significant bit to the corresponding bit in the message
#         image_data[i] = (image_data[i] & 0b11111110) | int(binary_message[counter])
#         counter += 1

#     # Save the modified image
#     with open(output_file, 'wb') as output:
#         output.write(image_data)

#     print(f"Message hidden successfully in {output_file}.")
#     return output_file


# def decode(image_path):
#     # Open the image file containing the hidden message
#     with open(image_path, "rb") as image_file:
#         image_data = bytearray(image_file.read())

#     # Extract the LSBs starting from the 54th byte
#     binary_message = "".join(str(image_data[i] & 1) for i in range(54, len(image_data)))

    
#     message = ""
#     for i in range(0, len(binary_message), 8):
#         byte = binary_message[i:i+8]
#         if len(byte) < 8:
#             break  
#         message += chr(int(byte, 2))

#     delimiter = message.find("###")
#     if delimiter != -1:
#         return message[:delimiter]
#     return "No hidden message found."


####################################################################################################3



def test_hide_message():
    original_image_path = "test_input.bmp"
    message = "Test Message"
    output_image_path = "output.bmp"
    
    with open(original_image_path, "wb") as image:
        image.write(bytearray([0] * 54 + [255] * 1000))

    result_image_path = hide_message(original_image_path, message)

    assert result_image_path == output_image_path, "Output file path is incorrect"

    hidden_message = decode(output_image_path)
    assert hidden_message == message, "Hidden message did not match the original"

def test_decode():
    original_image_path = "test_input.bmp"
    message = "Test Message"
    output_image_path = "output.bmp"

    with open(original_image_path, "wb") as image:
        image.write(bytearray([0] * 54 + [255] * 1000))  

    hide_message(original_image_path, message)

    hidden_message = decode(output_image_path)

    assert hidden_message == message, "Decoded message did not match the original"

def run_tests():
    try:
        test_hide_message()
        print("test_hide_message passed")
    except AssertionError as e:
        print(f"test_hide_message failed: {e}")

    try:
        test_decode()
        print("test_decode passed")
    except AssertionError as e:
        print(f"test_decode failed: {e}")

run_tests()
