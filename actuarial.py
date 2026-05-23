"""Prina Insurance — Actuarial Engine"""
import numpy as np

TMI = {
    "L": {
        0:5.24e-3,1:5.3e-4,2:4.2e-4,3:3.4e-4,4:2.9e-4,5:2.6e-4,6:2.3e-4,7:2.1e-4,8:2.0e-4,9:2.0e-4,
        10:1.9e-4,11:1.9e-4,12:1.9e-4,13:2.0e-4,14:2.3e-4,15:2.7e-4,16:3.1e-4,17:3.7e-4,18:4.3e-4,19:4.7e-4,
        20:4.9e-4,21:4.9e-4,22:4.9e-4,23:4.9e-4,24:5.0e-4,25:5.2e-4,26:5.5e-4,27:6.0e-4,28:6.5e-4,29:7.0e-4,
        30:7.5e-4,31:8.1e-4,32:8.7e-4,33:9.3e-4,34:9.9e-4,35:1.07e-3,36:1.16e-3,37:1.27e-3,38:1.39e-3,39:1.55e-3,
        40:1.73e-3,41:1.93e-3,42:2.16e-3,43:2.41e-3,44:2.70e-3,45:3.02e-3,46:3.38e-3,47:3.77e-3,48:4.18e-3,49:4.61e-3,
        50:5.08e-3,51:5.56e-3,52:6.09e-3,53:6.67e-3,54:7.27e-3,55:7.89e-3,56:8.47e-3,57:8.98e-3,58:9.39e-3,59:9.71e-3,
        60:9.99e-3,61:1.024e-2,62:1.046e-2,63:1.071e-2,64:1.104e-2,65:1.146e-2,66:1.199e-2,67:1.260e-2,68:1.329e-2,69:1.405e-2,
        70:1.485e-2,71:1.574e-2,72:1.670e-2,73:1.777e-2,74:1.895e-2,75:2.026e-2,76:2.369e-2,77:2.738e-2,78:3.130e-2,79:3.693e-2,80:4.518e-2,
    },
    "P": {
        0:2.66e-3,1:4.1e-4,2:3.1e-4,3:2.4e-4,4:2.1e-4,5:2.0e-4,6:2.2e-4,7:2.3e-4,8:2.2e-4,9:2.1e-4,
        10:1.9e-4,11:1.8e-4,12:2.0e-4,13:2.2e-4,14:2.3e-4,15:2.3e-4,16:2.4e-4,17:2.4e-4,18:2.5e-4,19:2.6e-4,
        20:2.7e-4,21:2.8e-4,22:3.0e-4,23:3.2e-4,24:3.4e-4,25:3.8e-4,26:4.2e-4,27:4.6e-4,28:4.9e-4,29:5.2e-4,
        30:5.6e-4,31:6.0e-4,32:6.4e-4,33:6.9e-4,34:7.4e-4,35:8.0e-4,36:8.6e-4,37:9.3e-4,38:1.00e-3,39:1.08e-3,
        40:1.18e-3,41:1.28e-3,42:1.41e-3,43:1.54e-3,44:1.69e-3,45:1.87e-3,46:2.09e-3,47:2.30e-3,48:2.53e-3,49:2.77e-3,
        50:3.05e-3,51:3.35e-3,52:3.68e-3,53:4.03e-3,54:4.42e-3,55:4.83e-3,56:5.24e-3,57:5.63e-3,58:6.01e-3,59:6.36e-3,
        60:6.71e-3,61:7.07e-3,62:7.46e-3,63:7.88e-3,64:8.33e-3,65:8.83e-3,66:9.40e-3,67:1.005e-2,68:1.076e-2,69:1.150e-2,
        70:1.229e-2,71:1.314e-2,72:1.406e-2,73:1.508e-2,74:1.620e-2,75:1.743e-2,76:1.879e-2,77:2.030e-2,78:2.326e-2,79:2.880e-2,80:3.569e-2,
    },
}

def lapse_rate(py):
    return 0.12 if py <= 2 else (0.07 if py <= 5 else 0.03)

def udd_4dec(q1p, q2p, q3p, q4p):
    qs = [q1p, q2p, q3p, q4p]
    result = []
    for j in range(4):
        o = [qs[k] for k in range(4) if k != j]
        a, b, c = o
        f = 1.0 - 0.5*(a+b+c) + (1/3)*(a*b+a*c+b*c) - (1/4)*a*b*c
        result.append(qs[j] * f)
    return tuple(result)

def compute(x, gender, SA, i, n=20, b3=1.0, max_iter=40, tol=1e-10):
    v = 1.0 / (1.0 + i)
    tmi = TMI[gender]
    q1,q2,q3,q4,ptau = [],[],[],[],[]
    asdt_rows = []
    for t in range(n):
        age = x + t
        q1p = tmi.get(age, 0.0)
        q2p, q3p_val, q4p = 0.10*q1p, 0.05*q1p, lapse_rate(t+1)
        a,b,c,d = udd_4dec(q1p, q2p, q3p_val, q4p)
        q1.append(a); q2.append(b); q3.append(c); q4.append(d)
        ptau.append(1.0 - a - b - c - d)
        asdt_rows.append({
            "Tahun":t+1,"Usia":age,
            "q'(1)":q1p,"q'(2)":q2p,"q'(3)":q3p_val,"q'(4)":q4p,
            "q(1)":a,"q(2)":b,"q(3)":c,"q(4)":d,
            "q(τ)":1-ptau[-1],"p(τ)":ptau[-1],
        })

    tpx = np.ones(n+1)
    for t in range(n): tpx[t+1] = tpx[t]*ptau[t]
    a_due = float(sum(v**t * tpx[t] for t in range(n)))
    denom = 0.78*a_due - 0.33
    if denom <= 0:
        raise ValueError("Suku bunga terlalu rendah untuk usia ini.")

    V = np.zeros(n+1); P_net = 0.0; iters = 0
    for it in range(max_iter):
        APV_B = sum((v**(t+1))*tpx[t]*(q1[t]*SA+q2[t]*2*SA+q3[t]*b3*SA+q4[t]*0.5*V[t+1]) for t in range(n))
        APV_B += (v**n)*tpx[n]*SA
        P_net_new = APV_B / a_due
        V_new = np.zeros(n+1)
        for k in range(n):
            Dk = q1[k]*SA + q2[k]*2*SA + q3[k]*b3*SA
            V_new[k+1] = ((V_new[k]+P_net_new)*(1+i) - Dk) / (0.5*q4[k]+ptau[k])
        iters = it+1
        if abs(P_net_new - P_net) < tol: P_net=P_net_new; V=V_new; break
        P_net=P_net_new; V=V_new

    P_gross = APV_B / denom
    APV_P   = P_gross * a_due
    APV_exp = P_gross * (0.33 + 0.07*a_due)

    return dict(
        P_gross=P_gross, P_net=P_net, V=V,
        tpx=tpx, a_due=a_due, APV_B=APV_B, APV_P=APV_P, APV_exp=APV_exp,
        profit=(APV_P-APV_B-APV_exp)/APV_P*100,
        iters=iters, asdt=asdt_rows,
        q1=q1, q2=q2, q3=q3, q4=q4, ptau=ptau,
    )
