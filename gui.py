import streamlit as st


class Gui:
    def __init__(self):
        self.configure_page()
        self.configure_styling()
        st.title("Sudoku Solver")
        self.puzzle_input()

    @staticmethod
    def configure_page():
        st.set_page_config(
            page_title="Sudoku Solver",
            page_icon=":jigsaw:",
            layout="wide"
        )

    @staticmethod
    def configure_styling():
        hide_st_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
        st.markdown(hide_st_style, unsafe_allow_html=True)

    @staticmethod
    def puzzle_input():
        ###################################################
        # Square Row 1
        ###################################################
        sr1_c1, sr1_c2, sr1_c3 = st.columns(3, gap="large")

        with sr1_c1:
            sr1_c1_1, sr1_c1_2, sr1_c1_3 = st.columns(3)

            with sr1_c1_1:
                st.number_input("1-1", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-1", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-1", min_value=0, max_value=9, label_visibility="collapsed")

            with sr1_c1_2:
                st.number_input("1-2", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-2", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-2", min_value=0, max_value=9, label_visibility="collapsed")

            with sr1_c1_3:
                st.number_input("1-3", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-3", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-3", min_value=0, max_value=9, label_visibility="collapsed")

        with sr1_c2:
            sr1_c2_1, sr1_c2_2, sr1_c2_3 = st.columns(3)

            with sr1_c2_1:
                st.number_input("1-4", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-4", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-4", min_value=0, max_value=9, label_visibility="collapsed")

            with sr1_c2_2:
                st.number_input("1-5", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-5", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-5", min_value=0, max_value=9, label_visibility="collapsed")

            with sr1_c2_3:
                st.number_input("1-6", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-6", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-6", min_value=0, max_value=9, label_visibility="collapsed")

        with sr1_c3:
            sr1_c3_1, sr1_c3_2, sr1_c3_3 = st.columns(3)

            with sr1_c3_1:
                st.number_input("1-7", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-7", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-7", min_value=0, max_value=9, label_visibility="collapsed")

            with sr1_c3_2:
                st.number_input("1-8", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-8", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-8", min_value=0, max_value=9, label_visibility="collapsed")

            with sr1_c3_3:
                st.number_input("1-9", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("2-9", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("3-9", min_value=0, max_value=9, label_visibility="collapsed")

        st.write("---")

        ###################################################
        # Square Row 2
        ###################################################
        sr2_c1, sr2_c2, sr2_c3 = st.columns(3, gap="large")

        with sr2_c1:
            sr2_c1_1, sr2_c1_2, sr2_c1_3 = st.columns(3)

            with sr2_c1_1:
                st.number_input("4-1", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-1", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-1", min_value=0, max_value=9, label_visibility="collapsed")

            with sr2_c1_2:
                st.number_input("4-2", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-2", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-2", min_value=0, max_value=9, label_visibility="collapsed")

            with sr2_c1_3:
                st.number_input("4-3", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-3", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-3", min_value=0, max_value=9, label_visibility="collapsed")

        with sr2_c2:
            sr2_c2_1, sr2_c2_2, sr2_c2_3 = st.columns(3)

            with sr2_c2_1:
                st.number_input("4-4", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-4", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-4", min_value=0, max_value=9, label_visibility="collapsed")

            with sr2_c2_2:
                st.number_input("4-5", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-5", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-5", min_value=0, max_value=9, label_visibility="collapsed")

            with sr2_c2_3:
                st.number_input("4-6", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-6", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-6", min_value=0, max_value=9, label_visibility="collapsed")

        with sr2_c3:
            sr2_c3_1, sr2_c3_2, sr2_c3_3 = st.columns(3)

            with sr2_c3_1:
                st.number_input("4-7", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-7", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-7", min_value=0, max_value=9, label_visibility="collapsed")

            with sr2_c3_2:
                st.number_input("4-8", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-8", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-8", min_value=0, max_value=9, label_visibility="collapsed")

            with sr2_c3_3:
                st.number_input("4-9", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("5-9", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("6-9", min_value=0, max_value=9, label_visibility="collapsed")

        st.write("---")

        ###################################################
        # Square Row 3
        ###################################################
        sr3_c1, sr3_c2, sr3_c3 = st.columns(3, gap="large")

        with sr3_c1:
            sr3_c1_1, sr3_c1_2, sr3_c1_3 = st.columns(3)

            with sr3_c1_1:
                st.number_input("7-1", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-1", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-1", min_value=0, max_value=9, label_visibility="collapsed")

            with sr3_c1_2:
                st.number_input("7-2", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-2", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-2", min_value=0, max_value=9, label_visibility="collapsed")

            with sr3_c1_3:
                st.number_input("7-3", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-3", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-3", min_value=0, max_value=9, label_visibility="collapsed")

        with sr3_c2:
            sr3_c2_1, sr3_c2_2, sr3_c2_3 = st.columns(3)

            with sr3_c2_1:
                st.number_input("7-4", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-4", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-4", min_value=0, max_value=9, label_visibility="collapsed")

            with sr3_c2_2:
                st.number_input("7-5", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-5", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-5", min_value=0, max_value=9, label_visibility="collapsed")

            with sr3_c2_3:
                st.number_input("7-6", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-6", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-6", min_value=0, max_value=9, label_visibility="collapsed")

        with sr3_c3:
            sr3_c3_1, sr3_c3_2, sr3_c3_3 = st.columns(3)

            with sr3_c3_1:
                st.number_input("7-7", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-7", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-7", min_value=0, max_value=9, label_visibility="collapsed")

            with sr3_c3_2:
                st.number_input("7-8", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-8", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-8", min_value=0, max_value=9, label_visibility="collapsed")

            with sr3_c3_3:
                st.number_input("7-9", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("8-9", min_value=0, max_value=9, label_visibility="collapsed")
                st.number_input("9-9", min_value=0, max_value=9, label_visibility="collapsed")


if __name__ == '__main__':
    Gui()
