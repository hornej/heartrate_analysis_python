import heartbeat as hb
hrdata = hb.get_data('data2.csv', column_name = 'hr')
timerdata = hb.get_data('data2.csv', column_name = 'timer')

hb.process(hrdata, hb.get_samplerate_mstimer(timerdata))

#plot with different title
hb.plotter(title='Heart Beat Detection on Noisy Signal')
