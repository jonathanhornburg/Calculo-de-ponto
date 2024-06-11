from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk
import openpyxl
from tkinter import messagebox


#layout
sg.theme('Reddit')
fonte_input=("Arial", 18)
fonte_text=("Arial", 15)
fonte_info=("Arial", 12)
# Nomes dos meses em português
meses_pt = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril',
    'Maio', 'Junho', 'Julho', 'Agosto',
    'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

# Nomes dos dias da semana em português
dias_semana_pt = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']

lado_2=[
  [sg.Table(values=[],  # Começando com uma tabela vazia
    headings=['Data', 'Entrada 1', 'Saida 1', 'Entrada 2', 'Saida 2', 'Soma', 'Hrs Faltas', 'Hrs Extras'],
    key='TABLE',
    auto_size_columns=False,
    display_row_numbers=False,
    justification='center',
    font =("Arial", 9),
    num_rows=18)],
  [sg.HorizontalSeparator(color='black')],
  [sg.Column([[sg.Text('Dias',font=fonte_info)],
      [sg.Input(key='dia',size=(2,1),default_text=0,font=fonte_info)]]),
  sg.VerticalSeparator(color='black'),
      sg.Column([[sg.Text('Soma',font=fonte_info)],
      [sg.Input(key='soma_hr',size=(3,1),justification='right',default_text=0,font=fonte_info),sg.Text(':',font=fonte_info),sg.Input(key='soma_min',size=(2,1),default_text=0,font=fonte_info)]],element_justification='center'),
  sg.VerticalSeparator(color='black'),
      sg.Column([[sg.Text('Hrs faltas',font=fonte_info)],
      [sg.Input(key='falta_hr',size=(3,1),justification='right',default_text=0,font=fonte_info),sg.Text(':',font=fonte_info),sg.Input(key='falta_min',size=(2,1),default_text=0,font=fonte_info)]],element_justification='center'),
   sg.VerticalSeparator(color='black'),
      sg.Column([[sg.Text('Hrs Extras',font=fonte_info)],
      [sg.Input(key='extra_hr',size=(3,1),justification='right',default_text=0,font=fonte_info),sg.Text(':',font=fonte_info),sg.Input(key='extra_min',size=(2,1),default_text=0,font=fonte_info)]],element_justification='center'),sg.Sizer(20, 0),sg.Button('Deletar Linha',font=fonte_input)
  ]
]

lado_1=[
  [sg.Column([[sg.Text('Nome',font=fonte_text)],
              [sg.Input(key='nome',size=(15,1),font=fonte_input)]]),
   sg.Column([[sg.CalendarButton('Data Inicio',font=("Arial", 8), target='date_input', format='%d/%m/%y', month_names=meses_pt, day_abbreviations=dias_semana_pt, key='calendar')],
              [sg.InputText('', key='date_input',font=fonte_input,size=(10,1))]])

  ],

  [sg.Text('Expediente',font=fonte_text),sg.HorizontalSeparator(color='black')],

  [sg.Column([[sg.Text('Inicio',font=fonte_text)],
      [sg.Input(key='expede_ini_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),sg.Input(key='expede_ini_min',size=(2,1),font=fonte_input)]],element_justification='center'),
   sg.VerticalSeparator(color='black'),
      sg.Column([[sg.Text('Intervalo',font=fonte_text)],
      [sg.Input(key='inter_ini_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),sg.Input(key='inter_ini_min',size=(2,1),font=fonte_input),sg.Sizer(10, 0),
      sg.Input(key='inter_fim_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),
      sg.Input(key='inter_fim_min',size=(2,1),font=fonte_input)]],element_justification='center'),
   sg.VerticalSeparator(color='black'),
      sg.Column([[sg.Text('Saida',font=fonte_text)],
      [sg.Input(key='expede_fim_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),sg.Input(key='expede_fim_min',size=(2,1),font=fonte_input)]],element_justification='center')
  ],

  [sg.Text('Marcação do Ponto',font=fonte_text),sg.HorizontalSeparator(color='black')],

  [sg.Column([[sg.Text('Entrada 1',font=fonte_text)],
      [sg.Input(key='ini_1_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),sg.Input(key='ini_1_min',size=(2,1),font=fonte_input)]],element_justification='center'),
   sg.VerticalSeparator(color='black'),
      sg.Column([[sg.Text('Saida 1',font=fonte_text)],
      [sg.Input(key='fim_1_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),sg.Input(key='fim_1_min',size=(2,1),font=fonte_input)]],element_justification='center'),
      sg.Column([[sg.Text('Entrada 2',font=fonte_text)],
      [sg.Input(key='ini_2_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),sg.Input(key='ini_2_min',size=(2,1),font=fonte_input)]],element_justification='center'),
   sg.VerticalSeparator(color='black'),
      sg.Column([[sg.Text('Saida 2',font=fonte_text)],
      [sg.Input(key='fim_2_hr',size=(2,1),font=fonte_input),sg.Text(':',font=fonte_text),sg.Input(key='fim_2_min',size=(2,1),font=fonte_input)]],element_justification='center')
  ],

  [sg.HorizontalSeparator(color='black')],

  [sg.Sizer(3, 0),sg.Button('Calcular',font=fonte_input),sg.Button('Folga',font=fonte_input),sg.Button('Limpar',font=fonte_input),sg.Button('Relatorio',font=fonte_input)]

]

layout=[
  sg.vtop([sg.Frame('',lado_1,border_width=7),sg.Frame('',lado_2,border_width=5)])
]
#janela
janela = sg.Window('Calculo de ponto', layout, finalize=True)
janela['expede_ini_hr'].bind("<Return>", "_Enter")
janela['expede_ini_min'].bind("<Return>", "_Enter")
janela['inter_ini_hr'].bind("<Return>", "_Enter")
janela['inter_ini_min'].bind("<Return>", "_Enter")
janela['inter_fim_hr'].bind("<Return>", "_Enter")
janela['inter_fim_min'].bind("<Return>", "_Enter")
janela['expede_fim_hr'].bind("<Return>", "_Enter")
janela['expede_fim_min'].bind("<Return>", "_Enter")
janela['ini_1_hr'].bind("<Return>", "_Enter")
janela['ini_1_min'].bind("<Return>", "_Enter")
janela['fim_1_hr'].bind("<Return>", "_Enter")
janela['fim_1_min'].bind("<Return>", "_Enter")
janela['ini_2_hr'].bind("<Return>", "_Enter")
janela['ini_2_min'].bind("<Return>", "_Enter")
janela['fim_2_hr'].bind("<Return>", "_Enter")
data = []
hist = []

def calc_intervalo(bat_hr,bat_min,expd_hr,exped_min,batida):
    if batida == 'fim':
        tempo = ((bat_hr*60)+bat_min)-((expd_hr*60)+exped_min)
    elif batida == 'inicio':
        tempo = ((expd_hr*60)+exped_min)-((bat_hr*60)+bat_min)
    else:
        tempo = 0

    if tempo > 0:
      extra = abs(tempo)
      falta = 0
    elif tempo < 0:
      falta = abs(tempo)
      extra = 0
    else:
      extra = 0
      falta = 0

    return extra,falta

def validar_campos(campo):
   
    if campo is None or campo == "":
      retorno =int(0)
    else:
        try:
            retorno = int(campo)
        except ValueError:
            root = tk.Tk()
            retorno = 0
            root.withdraw()  # Oculta a janela principal
            messagebox.showerror("Erro", "A entrada deve conter apenas números.")
            root.destroy()
    if len(campo) > 2:
        root = tk.Tk()
        retorno = 0
        root.withdraw()  # Oculta a janela principal
        messagebox.showerror("Erro", "A entrada contem mais de dois caracteres.")
        root.destroy()
    return retorno

#eventos
while True:
    eventos, valores = janela.read()
    ini_1_hr= validar_campos(valores['ini_1_hr'])
    ini_1_min= validar_campos(valores['ini_1_min'])
    fim_1_hr= validar_campos(valores['fim_1_hr'])
    fim_1_min= validar_campos(valores['fim_1_min'])
    ini_2_hr= validar_campos(valores['ini_2_hr'])
    ini_2_min= validar_campos(valores['ini_2_min'])
    fim_2_hr= validar_campos(valores['fim_2_hr'])
    fim_2_min= validar_campos(valores['fim_2_min'])
    soma_hr = validar_campos(valores['soma_hr'])
    soma_min = validar_campos(valores['soma_min'])

    falta_hr = validar_campos(valores['falta_hr'])
    falta_min = validar_campos(valores['falta_min'])
    extra_hr = validar_campos(valores['extra_hr'])
    extra_min = validar_campos(valores['extra_min'])
   
    expede_ini_hr= validar_campos(valores['expede_ini_hr'])
    expede_ini_min= validar_campos(valores['expede_ini_min'])
    inter_ini_hr= validar_campos(valores['inter_ini_hr'])
    inter_ini_min= validar_campos(valores['inter_ini_min'])
    inter_fim_hr= validar_campos(valores['inter_fim_hr'])
    inter_fim_min= validar_campos(valores['inter_fim_min'])
    expede_fim_hr= validar_campos(valores['expede_fim_hr'])
    expede_fim_min= validar_campos(valores['expede_fim_min'])
    dia = validar_campos(valores['dia'])
   
   
    if eventos == sg.WINDOW_CLOSED:
        break
       
    elif eventos == 'Relatorio':
        df = pd.DataFrame(data, columns=['Data','Entrada 1','Saida 1','Entrada 2','Saida 2','Soma','Hrs Faltas','Hrs Extras'])
        df.to_excel('teste.xlsx', index=False)
    elif eventos == 'Calcular':
        erro = 0
        if valores['date_input'] == "":
          dataformatada = '00/00/00'
        else:
            try:
                dataformatada = datetime.strptime(valores['date_input'], '%d/%m/%y').strftime
                date = datetime.strptime(valores['date_input'], '%d/%m/%y')
                date = date + timedelta(days=dia)
                dataformatada = date.strftime('%d/%m/%y')
            except ValueError:
                erro = 1
                root = tk.Tk()
                root.withdraw()  # Oculta a janela principal
                messagebox.showerror("Erro", "Data inválida.")
                root.destroy()
                 
        if erro == 0:        
            exped_temp = (((inter_ini_hr-expede_ini_hr)+(expede_fim_hr-inter_fim_hr))*60)+((inter_ini_min-expede_ini_min)+(expede_fim_min-inter_fim_min))
   
            tb_entra_1 = f"{'{:02d}'.format(ini_1_hr)}{':'}{'{:02d}'.format(ini_1_min)}"
            tb_saida_1 = f"{'{:02d}'.format(fim_1_hr)}{':'}{'{:02d}'.format(fim_1_min)}"
            tb_entra_2 = f"{'{:02d}'.format(ini_2_hr)}{':'}{'{:02d}'.format(ini_2_min)}"
            tb_saida_2 = f"{'{:02d}'.format(fim_2_hr)}{':'}{'{:02d}'.format(fim_2_min)}"
            if ini_1_hr == 0 and ini_1_min == 0 and fim_1_hr == 0 and fim_1_min == 0:
                batida_1 = [0,((inter_ini_hr-expede_ini_hr)*60)+(inter_ini_min-expede_ini_min)]
                batida_2 = [0,0]
            elif expede_ini_hr == 0 and expede_ini_min == 0 and inter_ini_hr == 0 and inter_ini_min == 0:
                batida_1 = [((fim_1_hr-ini_1_hr)*60)+(fim_1_min-ini_1_min),0]
                batida_2 = [0,0]
            else:
                batida_1 = calc_intervalo(ini_1_hr,ini_1_min,expede_ini_hr,expede_ini_min,'inicio')
                batida_2 = calc_intervalo(fim_1_hr,fim_1_min,inter_ini_hr,inter_ini_min,'fim')
   
            if ini_2_hr == 0 and ini_2_min == 0 and fim_2_hr == 0 and fim_2_min == 0:
                batida_3 = [0,((expede_fim_hr-inter_fim_hr)*60)+(expede_fim_min-inter_fim_min)]
                batida_4 = [0,0]
            elif inter_fim_hr == 0 and inter_fim_min == 0 and expede_fim_hr == 0 and expede_fim_min == 0:
                batida_3 = [((fim_2_hr-ini_2_hr)*60)+(fim_2_min-ini_2_min),0]
                batida_4 = [0,0]
            else:
                batida_3 = calc_intervalo(ini_2_hr,ini_2_min,inter_fim_hr,inter_fim_min,'inicio')
                batida_4 = calc_intervalo(fim_2_hr,fim_2_min,expede_fim_hr,expede_fim_min,'fim')
           
            if batida_1[0] < 5 and batida_2[0] < 5 and batida_3[0] < 5 and batida_4[0] < 5:
                valida_extra =   batida_1[0] + batida_2[0] + batida_3[0] + batida_4[0]
                if valida_extra < 10:
                    extra = 0
                else:
                    extra = valida_extra
            else:
                extra =   batida_1[0] + batida_2[0] + batida_3[0] + batida_4[0]
               
            tb_extra = f"{'{:02d}'.format(extra// 60)}{':'}{'{:02d}'.format(extra% 60)}"
   
            if batida_1[1] < 5 and batida_2[1] < 5 and batida_3[1] < 5 and batida_4[1] < 5:
                valida_falta = batida_1[1] + batida_2[1] + batida_3[1] + batida_4[1]
                if valida_falta < 10:
                    falta = 0
                else:
                    falta = valida_falta
            else:
                falta = batida_1[1] + batida_2[1] + batida_3[1] + batida_4[1]
           
            tb_falta = f"{'{:02d}'.format(falta// 60)}{':'}{'{:02d}'.format(falta% 60)}"
           
            total_soma  = exped_temp+extra-falta
            tb_soma = f"{'{:02d}'.format(total_soma// 60)}{':'}{'{:02d}'.format(total_soma% 60)}"
           
            hist.append([soma_hr, soma_min, falta_hr, falta_min, extra_hr, extra_min])
           
            total_ex_hr   = '{:02d}'.format(((extra_hr*60)+(extra+extra_min))   // 60)
            total_ex_min  = '{:02d}'.format(((extra_hr*60)+(extra+extra_min))   %  60)
            total_fal_hr  = '{:02d}'.format(((falta_hr*60)+(falta+falta_min))   // 60)
            total_fal_min = '{:02d}'.format(((falta_hr*60)+(falta+falta_min))   %  60)
            total_hr      = '{:02d}'.format(((soma_hr*60)+(total_soma+soma_min))// 60)
            total_min     = '{:02d}'.format(((soma_hr*60)+(total_soma+soma_min)) % 60)
   
   
            janela['extra_hr'].update(value=total_ex_hr)
            janela['extra_min'].update(value=total_ex_min)
            janela['falta_hr'].update(value=total_fal_hr)
            janela['falta_min'].update(value=total_fal_min)
            janela['soma_hr'].update(value=total_hr)
            janela['soma_min'].update(value=total_min)
   
   
            dia = dia+1
   
            data.append([dataformatada, tb_entra_1, tb_saida_1, tb_entra_2, tb_saida_2, tb_soma, tb_falta, tb_extra])
            janela['TABLE'].update(values=data)
            janela['dia'].update(value=dia)
            janela['ini_1_hr'].update(value='')
            janela['ini_1_min'].update(value='')
            janela['fim_1_hr'].update(value='')
            janela['fim_1_min'].update(value='')
            janela['ini_2_hr'].update(value='')
            janela['ini_2_min'].update(value='')
            janela['fim_2_hr'].update(value='')
            janela['fim_2_min'].update(value='')
            janela['ini_1_hr'].widget.focus_set()

    elif eventos == 'Folga':
        erro = 0
        if valores['date_input'] == "":
          dataformatada = '00/00/00'
        else:
            try:
                dataformatada = datetime.strptime(valores['date_input'], '%d/%m/%y').strftime
                date = datetime.strptime(valores['date_input'], '%d/%m/%y')
                date = date + timedelta(days=dia)
                dataformatada = date.strftime('%d/%m/%y')
            except ValueError:
                erro = 1
                root = tk.Tk()
                root.withdraw()  # Oculta a janela principal
                messagebox.showerror("Erro", "Data inválida.")
                root.destroy()
        if erro == 0:
            if ini_1_hr == 0 and ini_1_min == 0 and fim_1_hr == 0 and fim_1_min == 0 and ini_2_hr == 0 and ini_2_min == 0 and fim_2_hr == 0 and fim_2_min == 0:
                dia = dia+1
                data.append([dataformatada,'00:00', '00:00', '00:00', '00:00', '00:00', '00:00', '00:00'])
                hist.append([soma_hr, soma_min, falta_hr, falta_min, extra_hr, extra_min])
                janela['TABLE'].update(values=data)
                janela['dia'].update(value=dia)
            else:
                tb_entra_1 = f"{'{:02d}'.format(ini_1_hr)}{':'}{'{:02d}'.format(ini_1_min)}"
                tb_saida_1 = f"{'{:02d}'.format(fim_1_hr)}{':'}{'{:02d}'.format(fim_1_min)}"
                tb_entra_2 = f"{'{:02d}'.format(ini_2_hr)}{':'}{'{:02d}'.format(ini_2_min)}"
                tb_saida_2 = f"{'{:02d}'.format(fim_2_hr)}{':'}{'{:02d}'.format(fim_2_min)}"
                if ini_1_hr == 0 and ini_1_min == 0 and fim_1_hr == 0 and fim_1_min == 0:
                    batida_1 = [0,0]
                    batida_2 = [0,0]
                else:
                    batida_1 = [((fim_1_hr-ini_1_hr)*60)+(fim_1_min-ini_1_min),0]
                    batida_2 = [0,0]
               
   
                if ini_2_hr == 0 and ini_2_min == 0 and fim_2_hr == 0 and fim_2_min == 0:
                    batida_3 = [0,0]
                    batida_4 = [0,0]
                else:
                    batida_3 = [((fim_2_hr-ini_2_hr)*60)+(fim_2_min-ini_2_min),0]
                    batida_4 = [0,0]
               
   
                extra =   batida_1[0] + batida_2[0] + batida_3[0] + batida_4[0]
                tb_extra = f"{'{:02d}'.format(extra// 60)}{':'}{'{:02d}'.format(extra% 60)}"
                falta = batida_1[1] + batida_2[1] + batida_3[1] + batida_4[1]
                tb_falta = f"{'{:02d}'.format(falta// 60)}{':'}{'{:02d}'.format(falta% 60)}"
                total_soma  = extra
                tb_soma = f"{'{:02d}'.format(total_soma// 60)}{':'}{'{:02d}'.format(total_soma% 60)}"
   
                hist.append([soma_hr, soma_min, falta_hr, falta_min, extra_hr, extra_min])
               
                total_ex_hr   = '{:02d}'.format(((extra_hr*60)+(extra+extra_min))   // 60)
                total_ex_min  = '{:02d}'.format(((extra_hr*60)+(extra+extra_min))   %  60)
                total_fal_hr  = '{:02d}'.format(((falta_hr*60)+(falta+falta_min))   // 60)
                total_fal_min = '{:02d}'.format(((falta_hr*60)+(falta+falta_min))   %  60)
                total_hr      = '{:02d}'.format(((soma_hr*60)+(total_soma+soma_min))// 60)
                total_min     = '{:02d}'.format(((soma_hr*60)+(total_soma+soma_min)) % 60)
   
   
                janela['extra_hr'].update(value=total_ex_hr)
                janela['extra_min'].update(value=total_ex_min)
                janela['falta_hr'].update(value=total_fal_hr)
                janela['falta_min'].update(value=total_fal_min)
                janela['soma_hr'].update(value=total_hr)
                janela['soma_min'].update(value=total_min)
   
   
                dia = dia+1
   
                data.append([dataformatada, tb_entra_1, tb_saida_1, tb_entra_2, tb_saida_2, tb_soma, tb_falta, tb_extra])
                janela['TABLE'].update(values=data)
                janela['dia'].update(value=dia)
                janela['ini_1_hr'].update(value='')
                janela['ini_1_min'].update(value='')
                janela['fim_1_hr'].update(value='')
                janela['fim_1_min'].update(value='')
                janela['ini_2_hr'].update(value='')
                janela['ini_2_min'].update(value='')
                janela['fim_2_hr'].update(value='')
                janela['fim_2_min'].update(value='')
                janela['ini_1_hr'].widget.focus_set()
           

    elif eventos == 'Limpar':
        data = []
        hist = []
        janela['TABLE'].update(values=data)
        janela['nome'].update(value='')
        janela['date_input'].update(value='')
        janela['expede_ini_hr'].update(value='')
        janela['expede_ini_min'].update(value='')
        janela['inter_ini_hr'].update(value='')
        janela['inter_ini_min'].update(value='')
        janela['inter_fim_hr'].update(value='')
        janela['inter_fim_min'].update(value='')
        janela['expede_fim_hr'].update(value='')
        janela['expede_fim_min'].update(value='')
        janela['ini_1_hr'].update(value='')
        janela['ini_1_min'].update(value='')
        janela['fim_1_hr'].update(value='')
        janela['fim_1_min'].update(value='')
        janela['ini_2_hr'].update(value='')
        janela['ini_2_min'].update(value='')
        janela['fim_2_hr'].update(value='')
        janela['fim_2_min'].update(value='')
        janela['dia'].update(value=0)
        janela['soma_hr'].update(value=0)
        janela['soma_min'].update(value=0)
        janela['falta_hr'].update(value=0)
        janela['falta_min'].update(value=0)
        janela['extra_hr'].update(value=0)
        janela['extra_min'].update(value=0)
        janela['nome'].widget.focus_set()

    elif eventos == 'Deletar Linha':
        erro = 0
        try:
            data.pop()
            soma_hr_eli = hist[-1][0]
            soma_min_eli = hist[-1][1]
            falta_hr_eli = hist[-1][2]
            falta_min_eli = hist[-1][3]
            extra_hr_eli = hist[-1][4]
            extra_min_eli = hist[-1][5]
        except IndexError:
            root = tk.Tk()
            erro =1
            root.withdraw()  # Oculta a janela principal
            messagebox.showerror("Erro", "Não é possível remover a linha.")
            root.destroy()
        if erro == 0:
            janela['TABLE'].update(values=data)
            dia = dia-1
            janela['soma_hr'].update(value=soma_hr_eli)
            janela['soma_min'].update(value=soma_min_eli)
            janela['falta_hr'].update(value=falta_hr_eli)
            janela['falta_min'].update(value=falta_min_eli)
            janela['extra_hr'].update(value=extra_hr_eli)
            janela['extra_min'].update(value=extra_min_eli)
            janela['dia'].update(value=dia)
            hist.pop()



    elif eventos == "expede_ini_hr" + "_Enter":
        janela.Element('expede_ini_hr').TKEntry.tk_focusNext().focus_set()
    elif eventos == "expede_ini_min" + "_Enter":
        janela.Element('expede_ini_min').TKEntry.tk_focusNext().focus_set()
    elif eventos == "inter_ini_hr" + "_Enter":
        janela.Element('inter_ini_hr').TKEntry.tk_focusNext().focus_set()
    elif eventos == "inter_ini_min" + "_Enter":
        janela.Element('inter_ini_min').TKEntry.tk_focusNext().focus_set()
    elif eventos == "inter_fim_hr" + "_Enter":
        janela.Element('inter_fim_hr').TKEntry.tk_focusNext().focus_set()
    elif eventos == "inter_fim_min" + "_Enter":
        janela.Element('inter_fim_min').TKEntry.tk_focusNext().focus_set()
    elif eventos == "expede_fim_hr" + "_Enter":
        janela.Element('expede_fim_hr').TKEntry.tk_focusNext().focus_set()
    elif eventos == "expede_fim_min" + "_Enter":
        janela.Element('expede_fim_min').TKEntry.tk_focusNext().focus_set()
    elif eventos == "ini_1_hr" + "_Enter":
        janela.Element('ini_1_hr').TKEntry.tk_focusNext().focus_set()  
    elif eventos == "ini_1_min" + "_Enter":
        janela.Element('ini_1_min').TKEntry.tk_focusNext().focus_set()
    elif eventos == "fim_1_hr" + "_Enter":
        janela.Element('fim_1_hr').TKEntry.tk_focusNext().focus_set()
    elif eventos == "fim_1_min" + "_Enter":
        janela.Element('fim_1_min').TKEntry.tk_focusNext().focus_set()
    elif eventos == "ini_2_hr" + "_Enter":
        janela.Element('ini_2_hr').TKEntry.tk_focusNext().focus_set()  
    elif eventos == "ini_2_min" + "_Enter":
        janela.Element('ini_2_min').TKEntry.tk_focusNext().focus_set()
    elif eventos == "fim_2_hr" + "_Enter":
        janela.Element('fim_2_hr').TKEntry.tk_focusNext().focus_set()
