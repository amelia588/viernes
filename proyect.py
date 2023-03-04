Subtotal=Entry(miFrame, width=7, state="readonly")
Subtotal.grid(row=7, column=5, padx=10, pady=10)

TotalLabel=Label(miFrame,text="Total")
TotalLabel.grid(row=7, column=6, sticky="ew", padx=10, pady=10)

Total=Entry(miFrame, width=7, state="readonly")
Total.grid(row=7, column=7, padx=10, pady=10)

Guardar=Button(miFrame, text="Guardar")
Guardar.grid(row=8, column=2, padx=10, pady=10)