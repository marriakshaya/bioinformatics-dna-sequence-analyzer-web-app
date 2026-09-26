import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Bioinformatics DNA Sequence Analyzer",
    page_icon="🧬",
    layout="wide"
)


# ============================================================
# CUSTOM CSS - BIOINFORMATICS THEME
# ============================================================
st.markdown("""
<style>
.stApp { background: radial-gradient(circle at 10% 10%, rgba(14,165,233,.10), transparent 28%), radial-gradient(circle at 90% 15%, rgba(20,184,166,.10), transparent 28%), linear-gradient(135deg,#f0f9ff 0%,#ecfeff 50%,#f8fafc 100%); }
.block-container { padding-top:2rem; padding-bottom:3rem; max-width:1200px; }
.bio-header { background:linear-gradient(135deg,#075985,#0f766e); padding:30px 35px; border-radius:22px; text-align:center; margin-bottom:25px; box-shadow:0 10px 30px rgba(15,118,110,.20); }
.bio-header h1 { color:white !important; font-size:42px; font-weight:800; margin:0 0 10px 0; }
.bio-header p { color:#e0f2fe; font-size:18px; margin:0; }
h1,h2,h3 { color:#075985 !important; }
.stTextArea textarea { border:2px solid #bae6fd !important; border-radius:14px !important; background-color:rgba(255,255,255,.90) !important; font-family:monospace !important; font-size:16px !important; }
.stTextArea textarea:focus { border-color:#0f766e !important; box-shadow:0 0 0 2px rgba(15,118,110,.12) !important; }
.stButton > button { border-radius:12px; border:none; font-weight:700; padding:.65rem 1.4rem; transition:all .2s ease; }
.stButton > button[kind="primary"] { background:linear-gradient(135deg,#0284c7,#0f766e); color:white; box-shadow:0 5px 15px rgba(2,132,199,.25); }
.stButton > button:hover { transform:translateY(-2px); box-shadow:0 8px 20px rgba(2,132,199,.30); }
[data-testid="stMetric"] { background:rgba(255,255,255,.88); border:1px solid #bae6fd; border-radius:16px; padding:15px; box-shadow:0 5px 15px rgba(15,23,42,.06); }
.stTabs [data-baseweb="tab-list"] { gap:6px; background:rgba(255,255,255,.70); padding:8px; border-radius:14px; }
.stTabs [data-baseweb="tab"] { border-radius:10px; padding:10px 14px; font-weight:600; }
.stTabs [aria-selected="true"] { background:linear-gradient(135deg,#e0f2fe,#ccfbf1); color:#075985 !important; }
.stCodeBlock { border-radius:12px !important; border:1px solid #bae6fd !important; }
.stAlert { border-radius:12px !important; }
.stDownloadButton > button { width:100%; border-radius:12px; background:linear-gradient(135deg,#0f766e,#0284c7); color:white; font-weight:700; border:none; }
.stDownloadButton > button:hover { transform:translateY(-2px); }
hr { border-color:rgba(14,116,144,.18) !important; }
label { font-weight:600 !important; color:#164e63 !important; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# APP TITLE
# ============================================================
st.markdown(
    """
    <div class="bio-header">
        <h1>🧬 Bioinformatics DNA Sequence Analyzer</h1>
        <p>An interactive web tool for DNA sequence analysis, transformation, transcription and visualization.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ============================================================
# INPUT SECTION
# ============================================================
st.subheader("🧬 DNA Sequence Input")

dna_input = st.text_area(
    "Enter DNA Sequence:",
    value="ATGCCATCGATCGATCGATATTCCCTACCCCATATCCGCCTGA",
    height=120
)

# Clean sequence
dna = "".join(dna_input.upper().split())

# ============================================================
# ANALYZE BUTTON
# ============================================================
st.caption("Enter a DNA sequence containing only A, T, C, and G, then run the analysis.")

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

            if length < 3:

                st.warning(
                    "Please enter a DNA sequence with at least 3 bases "
                    "for codon analysis."
                )

            else:

                # Find the first start codon (ATG)
                start_index = dna.find("ATG")

                st.subheader("▶ Start Codon")

                if start_index != -1:

                    st.success(
                        f"✅ Valid start codon detected: ATG "
                        f"(position {start_index + 1})"
                    )

                    st.subheader("⏹ Stop Codon")

                    # Search for the first in-frame stop codon after ATG
                    stop_codon = None
                    stop_index = None

                    for i in range(start_index + 3, len(dna) - 2, 3):

                        codon = dna[i:i+3]

                        if codon in ["TAA", "TAG", "TGA"]:

                            stop_codon = codon
                            stop_index = i
                            break

                    if stop_codon:

                        st.success(
                            f"✅ Valid stop codon detected: {stop_codon} "
                            f"(position {stop_index + 1})"
                        )

                        # Show the identified coding region
                        coding_region = dna[start_index:stop_index + 3]

                        st.info(
                            f"🧬 Coding region: {coding_region}"
                        )

                    else:

                        st.warning(
                            "⚠️ No in-frame stop codon detected after "
                            "the start codon."
                        )

                else:

                    st.warning(
                        "⚠️ No valid start codon (ATG) detected."
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

