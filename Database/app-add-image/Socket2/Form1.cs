using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.IO;
namespace Socket2
{
    public partial class Form1 : Form
    {
        SqlConnection conn = new SqlConnection(@"Data Source=LAPTOP-2PGQ75MC\SQLEXPRESS;Initial Catalog=MMT_Lab;Persist Security Info=True;User ID=badhair;Password=123");
        public Form1()
        {
            InitializeComponent();
            loadData();
        }
        void loadData()
        {
            conn.Open();
            SqlCommand cmd = new SqlCommand("select * from STORE_DBS", conn);
            DataTable dt = new DataTable();
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            da.Fill(dt);
            dataGridView1.DataSource = dt;
            conn.Close();

        }

        private void Avatar_Click(object sender, EventArgs e)
        {
            OpenFileDialog open = new OpenFileDialog();
            open.Filter = "Select image(*.JpG; *.png; *.Gif)|*. JpG; *.png; *.Gif ";
            if (open.ShowDialog() == DialogResult.OK)
            {
                Avatar.Image = Image.FromFile(open.FileName);
                this.Text = open.FileName;
            }
           
        }

        private void button2_Click(object sender, EventArgs e)
        {
            byte[] b = ImageToByteArray(Avatar.Image);
            conn.Open();
            SqlCommand cmd = new SqlCommand("insert into STORE_DBS values(@Name,@MSSV,@Phone,@Gmail,@Avatar)", conn);
            cmd.Parameters.AddWithValue("@Name", NameText.Text);
            cmd.Parameters.AddWithValue("@MSSV", MSSVtext.Text);
            cmd.Parameters.AddWithValue("@Phone", PhoneText.Text);
            cmd.Parameters.AddWithValue("@Gmail", GmailText.Text);
            cmd.Parameters.AddWithValue("@Avatar", b);
            cmd.ExecuteNonQuery();
            conn.Close();
            MessageBox.Show("Data Inserted Successfully");
            loadData();
        }

        // c1. chuyen sang byte
        byte[] ImageToByteArray(Image img)
        {
            MemoryStream m = new MemoryStream();
            img.Save(m, System.Drawing.Imaging.ImageFormat.Png);
            return m.ToArray();
        }
    }
}
