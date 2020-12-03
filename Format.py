import xlsxwriter

def format_excel(writer, website):
    #Pegando dados a partir do escritor para trabalhar com xlsxwriter
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Criando formatações ---
    if website == 1:
        link_vcenter = workbook.add_format({'color': 'blue', 
                                            'underline': True, 
                                            'text_wrap': True,
                                            'valign' : 'vcenter',
                                            'align' : 'center'})

        text_vcenter = workbook.add_format({'text_wrap': True,
                                            'valign' : 'vcenter',
                                            'align' : 'center'})

        v_align = workbook.add_format({'text_wrap': True,
                                        'valign' : 'vcenter',
                                        'align' : 'center'})
        
        v_aling_yellow = workbook.add_format({'text_wrap': True,
                                            'bg_color': '#ffffbf',
                                            'valign' : 'vcenter',
                                            'align' : 'center'})

        text_vcenter_yellow = workbook.add_format({'bg_color': '#ffffbf',
                                            'text_wrap': True,
                                            'valign' : 'vcenter',
                                            'align' : 'center'})

        #Formatando ----
        worksheet.set_column('B:B', 25, text_vcenter)
        worksheet.set_column('C:C', 25, text_vcenter_yellow)
        worksheet.set_column('D:D', 20, text_vcenter)
        worksheet.set_column('E:E', 20, text_vcenter_yellow)
        worksheet.set_column('F:F', 20, text_vcenter)
        worksheet.set_column('G:G', 15, text_vcenter_yellow)
        worksheet.set_column('H:H', 20, text_vcenter)

    #Retornando writer com dados já formatados --- 
    return writer

