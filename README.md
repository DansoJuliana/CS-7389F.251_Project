# CS-7389F.251 Project

# 🔐 SteganoCrypt (LSB-RAS+AES): (LSB) Steganography with Hybrid (RSA+AES) Cryptography Tool

Description:<br>
This project implements a **secure image steganography system** that allows you to hide and extract files inside images using **hybrid cryptography (RSA+AES)** combined with **LSB (Least Significant Bit) embedding**. Thus, the project combines Asymmetric Cryptography (RSA), Symmetric Cryptography (AES-256), and LSB (Least Significant Bit) Steganography to hide sensitive files within images. This project ensures that even if a hidden file is detected, it remains unreadable without the corresponding private RSA key and passphrase.

---

## 📌 Functional Features

- Confidentiality via encryption  
- Imperceptibility via steganography  
- Efficiency via compression  
- Hide **any file** inside an image (PNG, BMP, TIFF, TGA)
- Extract hidden files securely using private key
- Hybrid encryption:
  - RSA (for key exchange)
  - AES-256 (for data encryption)
- Deterministic pixel embedding using seeded PRNG
- File compression using `zlib`
- Image quality evaluation using **MSE & PSNR**
- Batch processing support

## 📌 Technical Features

- **Hybrid Encryption**: Uses RSA-4096 (i.e., RSA-OAEP-Padding) to secure a session key and AES-256 (CBC mode) (i.e., AES-256-CBC) to encrypt the actual data.

- **Data Integrity**: PKCS7 Padding.

- **PBKDF2 Key Derivation for**: Strengthens security using 200,000 iterations of SHA-256.

- **Seeded Randomized LSB Steganography Embedding Method**: Data is not stored linearly. A PRNG (Pseudo-Random Number Generator) seeded by image dimensions scatters data bits across the image to resist visual and statistical analysis.  LSB Matching done on the Red channel (RGBA).

- **Randomization for LSB Embedding Method**: Fisher-Yates shuffle on pixel indices using a seed derived from width + height.

- **Compression**: Uses zlib to reduce the payload size before embedding.

- **Analysis Tools**: Includes scripts to calculate Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR) to measure image degradation.

---

## 🗂️ Project Structure

```
.
├── images/                 # Input/output images
├── generate_keys.py        # RSA key generation. Utility to create 4096-bit RSA key pairs.
├── main_steg.py            # Core steganography tool. The core engine for encryption
                              decryption, and LSB embedding.
├── MSE_PSNR.py             # Image quality evaluation. Calculates the mathematical difference 
                              between original and output images.
├── run.py                  # Batch processing script. Automation script for batch processing 
                              multiple images.
├── requirements.txt        # Dependencies. List of necessary Python libraries
                              (cryptography, Pillow, OpenCV (for computing MSE & PSNR), NumPy)
├── secret.txt              # Example file to hide
├── myprivatekey.pem        # Generated private key
├── mypublickey.pem         # Generated public key    
```
---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/JulianaMantebeaDanso/SteganoCrypt-tool.git
cd SteganoCrypt-tool
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
⚠️ Python requirements: Python 3.8+. Specifically, Python 3.9.25

---

## 🔑 Step 1: Generate RSA Keys

```bash
python generate_keys.py
```

You will be prompted for to enter an RSA Private Key Passphrase.

Output:
- `myprivatekey.pem` (encrypted)
- `mypublickey.pem`

---

## 🕵️ Step 2: Hide a File in an Image

```bash
python main_steg.py hide <host_image> <secret_file> <public_key> <output_image>
```

### Example:
```bash
python main_steg.py hide images/in1.png secret.txt mypublickey.pem images/out1.png
```

---

## 🔍 Step 3: Extract Hidden File

```bash
python main_steg.py extract <stego_image> <private_key> [output_file]
```

### Example:
```bash
python main_steg.py extract images/out1.png myprivatekey.pem extracted.txt
```

---

## 📊 Image Quality Evaluation

```bash
python MSE_PSNR.py
```

Metrics:
- MSE (Mean Squared Error) → Lower is better
- PSNR (Peak Signal-to-Noise Ratio) → Higher is better

Example Output:

<pre>
Image 1:
MSE  = 0.0021
PSNR = 74.12 dB
</pre>

---

## 🔁 Batch Processing

```bash
python run.py
```
- Processes multiple images automatically
- Skips missing files
- Measures execution time
---

## 📁 Supported Image Formats
- PNG
- BMP
- TIFF
- TGA

## ⚠️ Limitations
- Image and Text contents must be large enough to get optimal input. Example 4K
- Only lossless formats supported
- Sensitive to image modification (resizing/compression breaks extraction)
- Do not support JPEG (with robust embedding)

---

## 📊 Results & Evaluation

This section presents a comparison between the **proposed method (SteganoCrypt)** and the baseline **LSB_PLS** in terms of:

- ⏱️ Execution Time  
- 📉 Mean Squared Error (MSE)  
- 📈 Peak Signal-to-Noise Ratio (PSNR)  

---

## 🔐 SteganoCrypt (Proposed Method)

| Image | Time (seconds) | MSE | PSNR (dB) |
|------|----------------|------|-----------|
| Image 1 | 0.4606 | 0.0387 | 62.2526 |
| Image 2 | 0.5654 | 0.0112 | 67.6203 |
| Image 3 | 0.7016 | 0.0076 | 69.3488 |
| Image 4 | 0.7387 | 0.0101 | 68.1024 |
| Image 5 | 0.7549 | 0.0081 | 69.0554 |
| Image 6 | 9.8080 | 0.0003 | 83.1806 |
| Image 7 | 17.7793 | 0.0001 | 87.6739 |
| Image 8 | 3.0384 | 0.0008 | 79.0358 |
| Image 9 | 13.3037 | 0.0002 | 84.3432 |

---

## 🔓 LSB_PLS (Baseline Method)

| Image | Time (seconds) | MSE | PSNR (dB) |
|------|----------------|------|-----------|
| Image 1 | 0.1342 | 0.0973 | 58.2486 |
| Image 2 | 0.2505 | 0.0282 | 63.6330 |
| Image 3 | 0.3592 | 0.0188 | 65.4004 |
| Image 4 | 0.2548 | 0.0247 | 64.2109 |
| Image 5 | 0.3408 | 0.0200 | 65.1101 |
| Image 6 | 7.1385 | 0.0008 | 78.9903 |
| Image 7 | 20.6853 | 0.0003 | 83.7300 |
| Image 8 | 2.8216 | 0.0020 | 75.1186 |
| Image 9 | 8.7704 | 0.0006 | 80.4164 |

---

## 📌 Key Observations

- ✅ **Higher PSNR (Better Image Quality):**  
  SteganoCrypt consistently achieves higher PSNR values across all images.

- ✅ **Lower MSE (Less Distortion):**  
  The proposed method shows lower reconstruction error, especially for larger images.

- ⚖️ **Trade-off – Execution Time:**  
  SteganoCrypt is slightly slower due to encryption and compression overhead.

- 🔐 **Security Advantage:**  
  Hybrid encryption (RSA + AES) and randomized embedding make SteganoCrypt significantly more secure than LSB_PLS.

---

## 🏆 Conclusion

The **SteganoCrypt (Proposed Method)** provides:
- ✔️ Better image quality (higher PSNR)  
- ✔️ Lower distortion (lower MSE)  
- ✔️ Stronger security  

with a moderate increase in computational time.

## 👩‍💻 Author

**Juliana Mantebea Danso**  
PhD Student – Computer Science  
Texas State University  

---

## 📜 License

Note: This tool was developed as the resaerch and development part of the course CS-7389: SECURE CYBER PHYSICAL SYSTEMS of Texas State University. It is intended for educational and research purposes.
