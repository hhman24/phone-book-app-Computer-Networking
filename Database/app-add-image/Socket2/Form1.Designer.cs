
namespace Socket2
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Avatar = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.NameText = new System.Windows.Forms.TextBox();
            this.MSSVtext = new System.Windows.Forms.TextBox();
            this.PhoneText = new System.Windows.Forms.TextBox();
            this.GmailText = new System.Windows.Forms.TextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.Name = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.MSSV = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Phone = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Gmail = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.AvatarGriew = new System.Windows.Forms.DataGridViewImageColumn();
            ((System.ComponentModel.ISupportInitialize)(this.Avatar)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // Avatar
            // 
            this.Avatar.BackColor = System.Drawing.SystemColors.ActiveBorder;
            this.Avatar.Location = new System.Drawing.Point(25, 33);
            this.Avatar.Name = "Avatar";
            this.Avatar.Size = new System.Drawing.Size(246, 221);
            this.Avatar.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.Avatar.TabIndex = 0;
            this.Avatar.TabStop = false;
            this.Avatar.Click += new System.EventHandler(this.Avatar_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(326, 33);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(56, 22);
            this.label1.TabIndex = 2;
            this.label1.Text = "Name";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(326, 87);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(62, 22);
            this.label2.TabIndex = 3;
            this.label2.Text = "MSSV";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(326, 150);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(58, 22);
            this.label3.TabIndex = 4;
            this.label3.Text = "Phone";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(326, 208);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(59, 22);
            this.label4.TabIndex = 5;
            this.label4.Text = "Gmail";
            // 
            // NameText
            // 
            this.NameText.Location = new System.Drawing.Point(417, 30);
            this.NameText.Name = "NameText";
            this.NameText.Size = new System.Drawing.Size(360, 30);
            this.NameText.TabIndex = 6;
            // 
            // MSSVtext
            // 
            this.MSSVtext.Location = new System.Drawing.Point(417, 84);
            this.MSSVtext.Name = "MSSVtext";
            this.MSSVtext.Size = new System.Drawing.Size(360, 30);
            this.MSSVtext.TabIndex = 7;
            // 
            // PhoneText
            // 
            this.PhoneText.Location = new System.Drawing.Point(417, 147);
            this.PhoneText.Name = "PhoneText";
            this.PhoneText.Size = new System.Drawing.Size(360, 30);
            this.PhoneText.TabIndex = 8;
            // 
            // GmailText
            // 
            this.GmailText.Location = new System.Drawing.Point(417, 208);
            this.GmailText.Name = "GmailText";
            this.GmailText.Size = new System.Drawing.Size(360, 30);
            this.GmailText.TabIndex = 9;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(75, 260);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(102, 57);
            this.button2.TabIndex = 10;
            this.button2.Text = "button2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToAddRows = false;
            this.dataGridView1.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Name,
            this.MSSV,
            this.Phone,
            this.Gmail,
            this.AvatarGriew});
            this.dataGridView1.Location = new System.Drawing.Point(234, 295);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowHeadersWidth = 51;
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(778, 338);
            this.dataGridView1.TabIndex = 11;
            // 
            // Name
            // 
            this.Name.DataPropertyName = "Name";
            this.Name.HeaderText = "Name";
            this.Name.MinimumWidth = 6;
            this.Name.Name = "Name";
            // 
            // MSSV
            // 
            this.MSSV.DataPropertyName = "MSSV";
            this.MSSV.HeaderText = "MSSV";
            this.MSSV.MinimumWidth = 6;
            this.MSSV.Name = "MSSV";
            // 
            // Phone
            // 
            this.Phone.DataPropertyName = "Phone";
            this.Phone.HeaderText = "Phone";
            this.Phone.MinimumWidth = 6;
            this.Phone.Name = "Phone";
            // 
            // Gmail
            // 
            this.Gmail.DataPropertyName = "Gmail";
            this.Gmail.HeaderText = "Gmail";
            this.Gmail.MinimumWidth = 6;
            this.Gmail.Name = "Gmail";
            // 
            // AvatarGriew
            // 
            this.AvatarGriew.DataPropertyName = "Avatar";
            this.AvatarGriew.HeaderText = "Avatar";
            this.AvatarGriew.ImageLayout = System.Windows.Forms.DataGridViewImageCellLayout.Stretch;
            this.AvatarGriew.MinimumWidth = 6;
            this.AvatarGriew.Name = "AvatarGriew";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 22F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1097, 645);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.GmailText);
            this.Controls.Add(this.PhoneText);
            this.Controls.Add(this.MSSVtext);
            this.Controls.Add(this.NameText);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Avatar);
            this.Font = new System.Drawing.Font("Times New Roman", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Text = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.Avatar)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox Avatar;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox NameText;
        private System.Windows.Forms.TextBox MSSVtext;
        private System.Windows.Forms.TextBox PhoneText;
        private System.Windows.Forms.TextBox GmailText;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.DataGridViewTextBoxColumn Name;
        private System.Windows.Forms.DataGridViewTextBoxColumn MSSV;
        private System.Windows.Forms.DataGridViewTextBoxColumn Phone;
        private System.Windows.Forms.DataGridViewTextBoxColumn Gmail;
        private System.Windows.Forms.DataGridViewImageColumn AvatarGriew;
    }
}

