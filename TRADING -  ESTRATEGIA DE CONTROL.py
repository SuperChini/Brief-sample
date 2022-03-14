
import historical_volatility
import option_chain
import combo_entry_conditions
import entry_orders_from_contract_file
import entry_orders_completed_from_contract_file
import exit_orders_from_contract_file

def df_volatility(df, period):
 return (df.rolling(period).std() * np.sqrt(gv.period_1Y) * 100)

def df_minimum(df, period):
 return df.rolling(period).min()

date_2M = datetime.now().date() + relativedelta(months=2)
gv.taskDone.clear()
 optOrderId = app.nextOrderId()
 app.reqContractDetails(optOrderId, opt_contract)
 gv.taskDone.wait()
 gv.optMaturityDateList.sort()
 dateList = intersect(gv.optMaturityDateList, opt_exp_cal)
 dateList.sort()
 optMaturityDate = min(x for x in dateList if x >= minMaturityDate)
 opt_contract.lastTradeDateOrContractMonth = optMaturityDate
 ### Select strikes
 gv.optStrikesList = []
 gv.taskDone.clear()
 optOrderId = app.nextOrderId()
 app.reqContractDetails(optOrderId, opt_contract)
 gv.taskDone.wait()
 gv.optStrikesList.sort()
 strike_low = max(x for x in gv.optStrikesList if x <= stockPrice)

date_2M = comboPrices.iloc[-1].name - relativedelta(months=2)
 date_1M = comboPrices.iloc[-1].name - relativedelta(months=1)
 minComboPrice_3M = min(comboPrices['Close'])
comboPeriod = combo[2]
 comboQuantity = round(entry_parameters[comboPeriod][ep.Amount] /
 (comboPrices['Close'].iloc[-1] * 100))

if gv.order_status[ordId][2] == 0.0:
 combo_entry_order_submitted[0].extend(['COMPLETED - BUY MKT',
 gv.order_status[ordId][1],
 gv.order_status[ordId][2],
 gv.order_status[ordId][3]])
 combo_entry_order_completed.append(combo_entry_order_submitted[0])

 with open('file_combo_entry_order_completed', 'wb') as f:
     if gv.order_status[ordId][1] != 0.0:
         app.cancelOrder(ordId)
         combo_entry_order_submitted[0].extend(['PARTIAL - BUY MKT', gv.order_status[ordId][1], gv.order_status[ordId][2], gv.order_status[ordId][3]])
         combo_entry_order_completed.append(combo_entry_order_submitted[0])
         with open('file_combo_entry_order_completed', 'wb') as f:
             pickle.dump(combo_entry_order_completed, f)
         f.close()
         combo_entry_order_submitted.remove(combo_entry_order_submitted[0])
         with open('file_combo_entry_order_submitted', 'wb') as f:
             pickle.dump(combo_entry_order_submitted, f)
         f.close()
     else:
         app.cancelOrder(ordId)
         combo_entry_order_submitted[0].extend(['CANCELLED - BUY MKT', gv.order_status[ordId][1], gv.order_status[ordId][2],

                                                gv.order_status[ordId][3]])
         combo_entry_order_cancelled.append(combo_entry_order_submitted[0])
         with open('file_combo_entry_order_cancelled', 'wb') as f:
             pickle.dump(combo_entry_order_cancelled, f)
         f.close()
         combo_entry_order_submitted.remove(combo_entry_order_submitted[0])
         with open('file_combo_entry_order_submitted', 'wb') as f:
             pickle.dump(combo_entry_order_submitted, f)
         f.close()

         ### Recover entry order contract, quantity and average fill price
         contract = combo[cp.ComboContract]
         periodMin = combo[cp.PeriodMin]
         quantity = combo[cp.Filled]
         avgFillPrice = combo[cp.AverageFillPrice]

         ### Calculate stop loss and profit target
         pt_price = round(avgFillPrice * (1.0 + entry_parameters[periodMin][ep.Target]), 2)

         ### Send PT order
         pt_order = app.LimitOrder("SELL", quantity, pt_price)
         pt_order.tif = 'GTC'
         app.simplePlaceOid = app.nextOrderId()
         combo_entry_order_completed[0].extend([app.simplePlaceOid])
         app.placeOrder(app.simplePlaceOid, contract, pt_order)
     49
     combo_entry_order_completed[0].extend(['SUBMITTED - SELL LMT', quantity, pt_price])

