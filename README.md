# 🧬 Bioinformatics DNA Sequence Analyzer Web App

An interactive **Streamlit-based web application** for DNA sequence analysis using Python and basic bioinformatics concepts.

## 📌 About the Project

The **Bioinformatics DNA Sequence Analyzer Web App** is an interactive tool designed to perform common DNA sequence analysis tasks.

Users can enter a DNA sequence containing **A, T, C, and G** bases and analyze the sequence through an easy-to-use web interface.

The application provides nucleotide composition analysis, DNA sequence transformations, codon analysis, RNA transcription, CpG and motif analysis, visualization, and downloadable reports.

---

## ✨ Features

### 📊 Basic DNA Analysis
-	DNA sequence validation
-	Sequence length calculation
-	A, T, C, and G nucleotide counts
-	Nucleotide percentage calculation
-	GC content
-	AT content
-	GC/AT ratio

### 🧬 DNA Sequence Transformation
-	Complementary DNA sequence
-	Reverse DNA sequence
-	Reverse complement sequence

### 🔤 Codon Analysis
-	Start codon detection
-	Stop codon detection
-	Codon breakdown
-	Identification of the start codon ATG
-	Identification of stop codons TAA, TAG, and TGA

### 🔬 RNA Transcription
-	DNA-to-RNA transcription
-	Conversion of Thymine (T) to Uracil (U)

### 🔎 Sequence Features
- Custom DNA motif search
- Motif position detection
- CpG site analysis
- CpG position detection
-	GC/AT ratio analysis

### 📈 Visualization & Report
- Nucleotide composition chart
- GC content visualization
- DNA analysis summary
- Downloadable analysis report

## 🖥️ Application Interface

The application is organized into six separate tabs:

```text
DNAInsight
│
├── 📊 Basic Analysis
├── 🧬 Transformation
├── 🔤 Codon Analysis
├── 🔬 RNA Transcription
├── 🔎 Sequence Features
└── 📈 Visualization & Report
```

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Matplotlib**
* **Bioinformatics concepts**
* **DNA sequence analysis**

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/DNAInsight.git
```

### 2. Navigate to the Project Directory

```bash
cd DNAInsight
```

### 3. Install Required Libraries

```bash
pip install streamlit matplotlib
```

## ▶️ Run the Application

Run the following command:

```bash
streamlit run dna_analyzer.py
```

The application will open in your default web browser.

## 🧬 Example DNA Sequence

You can test the application using:

```text
ATGCCATCGATCGATCGATATTCCCTACCCCATATCCGCCTGA
```

The application will analyze the sequence and display:

* Sequence length
* Nucleotide composition
* GC content
* AT content
* Complement
* Reverse sequence
* Reverse complement
* RNA sequence
* Start and stop codons
* CpG sites
* Custom motifs
* Visualizations
* Analysis report

## 📂 Project Structure

```text
DNAInsight/
│
├── dna_analyzer.py
├── README.md
└── requirements.txt
```

## 🎯 Project Objectives

The main objectives of DNAInsight are:

1. To develop an interactive tool for DNA sequence analysis.
2. To provide commonly used bioinformatics sequence-processing functions.
3. To simplify DNA sequence analysis through a user-friendly web interface.
4. To calculate nucleotide composition and GC/AT content.
5. To analyze codons and perform DNA-to-RNA transcription.
6. To identify motifs and CpG sites.
7. To visualize DNA sequence characteristics.
8. To generate downloadable analysis reports.

## 🔬 Applications

DNAInsight can be useful for:

* Bioinformatics learning
* Biotechnology education
* Molecular biology coursework
* DNA sequence exploration
* Basic sequence analysis
* Motif identification
* Computational biology demonstrations
* Teaching DNA sequence concepts

## 👩‍💻 Author

**Marri Akshaya**

