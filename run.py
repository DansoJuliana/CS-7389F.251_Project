import os
import time

for i in range(1, 10):
    input_image = f"images/in{i}.png"
    output_image = f"images/out{i}.png"
    
    if not os.path.exists(input_image):
        print(f"\n{input_image} is not present")
        continue  # skip to next image
    
    command = f"python main_Steg.py hide {input_image} secret.txt mypublickey.pem {output_image}"
    
    print(f"\nProcessing Image {i}...")
    
    start_time = time.time()
    os.system(command)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Time taken for Image {i}: {elapsed_time:.4f} seconds")