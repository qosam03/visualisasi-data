import streamlit as st

st.header("Ini Header")
st.subheader("Ini sub Header")
st.text("ini tekas biasa tanpa format")
st.markdown("**ini teks bold** dan*ini teks italic*")
st.caption("ini caption")
st.title("ini judul")

#menampilkan rumus
st.header("Display latex")
st.latex(r'''\cos^2\theta = 1-2\sin^2\theta''')#rumus triogometri
st.latex(r"""(a+b)^2 = a^2 + b^2 + 2ab""")#rumus kuadrat
st.latex(r'''\frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}
+ \frac{\partial^2 u}{\partial z^2} \right)''')

#menampilkan kode program
st.header("dislpay kode")
st.subheader("python kode")

#simpan variable
code = '''
def hello():
print("hello,streamlit")
'''
#st.code untuk menampikan format rapih  syntax higliting
st.code(code,language='python')

st.subheader("""java code""")
st.code("""public class GFG{
    public static void main(string arg[]){system.out.printin(Hello word);
    }
}
""",language='javascript')

#fungsi st.code() bisa digunakan untuk bahasa pemograman lain seperti jawva, java sript, dll

st.subheader("""javascript code""")
st.code("""<p id="demo"><\p>
        <script>
        try{
            addlert(welcome guest!);// kesalahan ketik(addlaert)
            segaja dibuat untuk menimbulkan error
            }
            Catch(err){
                document.getElementById(demo).innerHtml = err.massage;//
            }
        </script>""")
