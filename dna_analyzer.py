import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="DNAInsight",
    page_icon="🧬",
    layout="wide"
)

# ============================================================
# APP TITLE
# ============================================================
st.title("🧬 DNAInsight")
st.write(
    "An interactive bioinformatics tool for DNA sequence analysis, "
    "transcription, codon analysis, and sequence transformation."
)

st.divider()

# ============================================================
# INPUT SECTION
# ============================================================
dna_input = st.text_area(
    "Enter DNA Sequence:",
    value="AATTCCGTA",
    height=120,
    placeholder="Example: ATGCGTACCGTAA"
)

# Clean sequence
dna = "".join(dna_input.upper().split())

# ============================================================
# ANALYZE BUTTON
# ============================================================
analyze = st.button(
    "🔬 Analyze DNA Sequence",
    type="primary"
)

# ============================================================
# VALIDATION
# ============================================================
if analyze:

    valid_bases = {"A", "T", "C", "G"}

    if not dna:
        st.error("⚠️ Please enter a DNA sequence.")

    elif not set(dna).issubset(valid_bases):
        st.error(
            "⚠️ Invalid DNA sequence. "
            "Please use only A, T, C, and G bases."
        )

    else:

        # ====================================================
        # BASIC CALCULATIONS
        # ====================================================
        length = len(dna)

        count_a = dna.count("A")
        count_t = dna.count("T")
        count_c = dna.count("C")
        count_g = dna.count("G")

        gc_content = ((count_g + count_c) / length) * 100
        at_content = ((count_a + count_t) / length) * 100

        # ====================================================
        # COMPLEMENT
        # ====================================================
        complement_map = {
            "A": "T",
            "T": "A",
            "G": "C",
            "C": "G"
        }

        complement = "".join(
            complement_map[base] for base in dna
        )

        reverse = dna[::-1]

        reverse_complement = complement[::-1]

        # ====================================================
        # RNA TRANSCRIPTION
        # ====================================================
        rna = dna.replace("T", "U")

        # ====================================================
        # TABS
        # ====================================================
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📊 Basic Analysis",
            "🧬 Transformation",
            "🔤 Codon Analysis",
            "🔬 RNA Transcription",
            "🔎 Sequence Features",
            "📈 Visualization & Report"
        ])

        # ====================================================
        # TAB 1 - BASIC ANALYSIS
        # ====================================================
        with tab1:

            st.header("📊 Basic DNA Analysis")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Sequence Length",
                f"{length} bp"
            )

            col2.metric(
                "GC Content",
                f"{gc_content:.2f}%"
            )

            col3.metric(
                "AT Content",
                f"{at_content:.2f}%"
            )

            st.divider()

            st.subheader("🧬 Nucleotide Composition")

            col_a, col_t, col_c, col_g = st.columns(4)

            col_a.metric("Adenine (A)", count_a)
            col_t.metric("Thymine (T)", count_t)
            col_c.metric("Cytosine (C)", count_c)
            col_g.metric("Guanine (G)", count_g)

            st.divider()

            st.subheader("📊 Nucleotide Percentages")

            a_percent = (count_a / length) * 100
            t_percent = (count_t / length) * 100
            c_percent = (count_c / length) * 100
            g_percent = (count_g / length) * 100

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("A %", f"{a_percent:.2f}%")
            col2.metric("T %", f"{t_percent:.2f}%")
            col3.metric("C %", f"{c_percent:.2f}%")
            col4.metric("G %", f"{g_percent:.2f}%")

            st.divider()

            st.subheader("📄 Input DNA Sequence")

            st.code(dna, language="text")

        # ====================================================
        # TAB 2 - SEQUENCE TRANSFORMATION
        # ====================================================
        with tab2:

            st.header("🧬 DNA Sequence Transformation")

            st.subheader("Original DNA")
            st.code(dna, language="text")

            st.subheader("Complementary DNA")
            st.code(complement, language="text")

            st.subheader("Reverse DNA")
            st.code(reverse, language="text")

            st.subheader("Reverse Complement")
            st.code(reverse_complement, language="text")

            st.info(
                "The reverse complement is obtained by taking the "
                "complementary sequence and reversing its direction."
            )

        # ====================================================
        # TAB 3 - CODON ANALYSIS
        # ====================================================
        with tab3:

            st.header("🔤 Start & Stop Codon Analysis")

            if length < 6:

                st.warning(
                    "Please enter a DNA sequence with at least 6 bases "
                    "for start and stop codon analysis."
                )

            else:

                start_codon = dna[:3]
                stop_codon = dna[-3:]

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Start Codon",
                        start_codon
                    )

                with col2:
                    st.metric(
                        "Stop Codon",
                        stop_codon
                    )

                st.divider()

                st.subheader("▶ Start Codon")

                if start_codon == "ATG":

                    st.success(
                        "✅ Valid start codon detected: ATG"
                    )

                else:

                    st.warning(
                        f"⚠️ No valid start codon detected. "
                        f"The sequence starts with {start_codon}."
                    )

                st.subheader("⏹ Stop Codon")

                if stop_codon in ["TAA", "TAG", "TGA"]:

                    st.success(
                        f"✅ Valid stop codon detected: {stop_codon}"
                    )

                else:

                    st.warning(
                        f"⚠️ No valid stop codon detected. "
                        f"The sequence ends with {stop_codon}."
                    )

                st.divider()

                st.subheader("🧬 Codon Breakdown")

                codons = [
                    dna[i:i+3]
                    for i in range(0, len(dna) - 2, 3)
                ]

                st.write(" | ".join(codons))

                st.info(
                    f"Total complete codons: {len(codons)}"
                )

        # ====================================================
        # TAB 4 - RNA TRANSCRIPTION
        # ====================================================
        with tab4:

            st.header("🔬 DNA to RNA Transcription")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("DNA Sequence")

                st.code(
                    dna,
                    language="text"
                )

            with col2:

                st.subheader("RNA Sequence")

                st.code(
                    rna,
                    language="text"
                )

            st.divider()

            st.success(
                "✅ DNA has been transcribed into RNA by replacing "
                "Thymine (T) with Uracil (U)."
            )

        # ====================================================
        # TAB 5 - SEQUENCE FEATURES
        # ====================================================
        with tab5:

            st.header("🔎 Sequence Features")

            # GC / AT Ratio
            st.subheader("📊 GC / AT Ratio")

            if at_content != 0:

                gc_at_ratio = gc_content / at_content

                st.metric(
                    "GC / AT Ratio",
                    f"{gc_at_ratio:.2f}"
                )

            else:

                st.warning(
                    "AT content is zero, so GC/AT ratio cannot be calculated."
                )

            # CpG Analysis
            st.divider()

            st.subheader("🧬 CpG Analysis")

            cpg_count = dna.count("CG")

            st.metric(
                "CpG Sites",
                cpg_count
            )

            if cpg_count > 0:

                cpg_positions = []

                for i in range(len(dna) - 1):

                    if dna[i:i+2] == "CG":

                        cpg_positions.append(i + 1)

                st.write(
                    "CpG positions:",
                    cpg_positions
                )

            else:

                st.info(
                    "No CpG sites detected."
                )

            # Motif Search
            st.divider()

            st.subheader("🔍 Motif Search")

            motif = st.text_input(
                "Enter a DNA motif to search:",
                value="ATG"
            ).upper().strip()

            if motif:

                positions = []

                for i in range(
                    len(dna) - len(motif) + 1
                ):

                    if dna[i:i+len(motif)] == motif:

                        positions.append(i + 1)

                if positions:

                    st.success(
                        f"Motif '{motif}' found "
                        f"{len(positions)} time(s)."
                    )

                    st.write(
                        "Positions:",
                        positions
                    )

                else:

                    st.warning(
                        f"Motif '{motif}' was not found."
                    )

        # ====================================================
        # TAB 6 - VISUALIZATION & REPORT
        # ====================================================
        with tab6:

            st.header("📈 DNA Visualization & Report")

            import matplotlib.pyplot as plt

            # Nucleotide Chart
            st.subheader("📊 Nucleotide Composition Chart")

            bases = ["A", "T", "C", "G"]

            counts = [
                count_a,
                count_t,
                count_c,
                count_g
            ]

            fig, ax = plt.subplots()

            ax.bar(bases, counts)

            ax.set_xlabel("Nucleotide")
            ax.set_ylabel("Count")
            ax.set_title("DNA Nucleotide Composition")

            st.pyplot(fig)

            # GC Content
            st.subheader("📈 GC Content")

            st.progress(
                min(gc_content / 100, 1.0)
            )

            st.write(
                f"GC Content: {gc_content:.2f}%"
            )

            # Analysis Report
            st.divider()

            st.subheader("📄 Analysis Summary")

            report = f"""
DNAINSIGHT ANALYSIS REPORT
===========================

Sequence Length: {length} bp

Nucleotide Counts:
A = {count_a}
T = {count_t}
C = {count_c}
G = {count_g}

GC Content: {gc_content:.2f}%
AT Content: {at_content:.2f}%

RNA Sequence:
{rna}

Complement:
{complement}

Reverse:
{reverse}

Reverse Complement:
{reverse_complement}

CpG Sites:
{cpg_count}
"""

            st.code(
                report,
                language="text"
            )

            st.download_button(
                label="⬇️ Download Analysis Report",
                data=report,
                file_name="dna_analysis_report.txt",
                mime="text/plain"
            )

# ====================================================
# SUCCESS MESSAGE
# ====================================================
st.success("✅ DNA sequence analysis completed successfully!")

