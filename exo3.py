import ftplib

# Open a connection to the FTP server
connexionftp = ftplib.FTP("ftp.vim.org")
print('\n######### Fin instruction [connexionftp=ftplib.FTP("ftp.vim.org")]\n')

# Perform anonymous login
connexionftp.login()
print('\n######### Fin instruction [connexionftp.login()]\n')

# List directory contents
print('\n'.join(connexionftp.nlst()))
print('\n######### Fin instruction [connexionftp.nlst()]\n')

# Navigate directories
print(connexionftp.cwd("pub"))
print(connexionftp.cwd("ImageMagick"))
print('\n######### Fin instruction CD pub\\ImageMagick')

# Download a file
connexionftp.retrbinary(
    'RETR ImageMagick-6.9.11-29.7z', open('ImageMagick-6.9.11-29.7z', 'wb').write
)
print('\n######### Fin instruction [ftp.retrbinary(...)]\n')
