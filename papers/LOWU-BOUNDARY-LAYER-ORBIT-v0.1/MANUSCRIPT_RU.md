# Низко-`u` гранично-слойная орбитальная механика для автономного реле Навье–Стокса

**Версия:** v0.1, кандидат к публикации  
**Дата:** 16.09.2026  
**Автор:** Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Репозиторий:** `AIDevelopersMonster/SOL-UNFORCED-NS`  
**Исследовательский срез:** `9add88598582959095c418a252a5d0d13ed9596f`

## Аннотация

Исследуется низкопараметрический гранично-слойный механизм реле для трёхмерных несжимаемых уравнений Навье–Стокса в геометрии, связанной с формализованной OpenAI конструкцией вынужденного blow-up. Настоящая работа **не** заявляет невынужденную сингулярность и **не** является решением задачи тысячелетия Навье–Стокса. Цель уже иная: выделить локальный Fourier-орбитальный механизм, который реализуем из начальных данных Коши и не использует будущие временные управляющие профили.

Механизм организован beta-(2,1) reset-shear и инвариантным beta-zero характером

\[
M=P-2C.
\]

В режиме малого `u` обнаружен гранично-слойный масштаб

\[
\delta_S=\kappa/S,
\]

при котором beta-one catalyst и beta-two parent допускают совместное двустороннее орбитальное описание. В рабочей точке

\[
u=1.8,\qquad x=0.70
\]

получены явные предельные операторы Пуанкаре, настроена совместимость через один beta-zero root и поперечную поляризацию, доказана физическая гауссова локализация центрального профиля и построены phase-adapted whole-space оценки Leray/Oseen для designated mean root и остаточной mean/nonzero correction.

Затем возникает структурное препятствие: никакой ненулевой конечноподдержанный bilateral orbit vector не может быть точным fixed vector предельного reset-оператора. Поскольку физический primary source bank при каждом конечном `S` имеет компактную поддержку по slope, точный compact-primary-bank reset невозможен уже на principal homogeneous level. Следовательно корректный локальный объект имеет вид **core + analytic tail**.

Дополнительно доказано, что предельный tail-оператор спектрально отделён от нестабильности центрального tangent-Gaussian пространства и обратим в weighted Wiener lattice при `sigma_0=0.005`.

Открытым остаётся finite-`S` variable-coefficient Lyapunov–Schmidt theorem, который должен достроить центральный tangent-Gaussian core экспоненциально малым analytic tail. До закрытия этого шага exact full-state finite-`S` reset не заявляется.

## 1. Границы утверждений

В этой статье не доказываются:

1. глобальная невынужденная сингулярность Навье–Стокса;
2. бесконечная forward cascade;
3. точный finite-`S` compact-primary-bank fixed point;
4. решение задачи Clay.

Доказываются более локальные и проверяемые утверждения:

- low-`u` beta-(2,1) boundary-layer mechanism допускает физически допустимый tangent-Gaussian центральный профиль;
- один Cauchy-realizable beta-zero root может генерировать нужные beta-one и beta-two орбитальные сдвиги после настройки поляризации;
- source/physical residual bridge, whole-space Leray, mean/nonzero correction и fixed-order bilinear estimates совместимы с этой архитектурой;
- ненулевой finite-support orbit exact reset невозможен;
- limiting analytic tail operator обратим в выбранном weighted Wiener space.

## 2. Исходная source-архитектура

Используется формализованная система `openai/NavierStokesAndEuler`, где присутствуют:

- dyadic scales `Q(n)=2^{-n}`;
- stage length `S(n)`;
- `epsilon=Q^h`;
- exact common-graph pullback к физическому residual;
- phase-adapted harmonic и mean classes;
- whole-space Leray projection;
- source-localized wave/covariance estimates.

Ключевой факт: `epsilon Delta` в graph equation является коэффициентом точного coordinate pullback, а не изменением физической вязкости. Физический residual остаётся viscosity-one Navier–Stokes residual.

## 3. Reset algebra

Пусть

\[
\beta(P)=2,
\qquad
\beta(C)=1.
\]

Reset действует так:

\[
R(P)=3P-4C,
\qquad
R(C)=P-C.
\]

Определим

\[
\boxed{M=P-2C.}
\]

Тогда для любого lattice character `K`

\[
\boxed{R(K)=K+\beta(K)M.}
\]

и, поскольку

\[
\beta(M)=0,
\]

получаем

\[
\boxed{R(M)=M.}
\]

Характер `M` относится к angular-mean sector. Поэтому он должен рассматриваться не как nonzero harmonic control, а как designated mean root, который сдвигает beta-one и beta-two орбиты.

Определим

\[
C_j=C+jM,
\qquad
Q_n=P+nM.
\]

Тогда

\[
R(C_j)=C_{j+1},
\qquad
R(Q_n)=Q_{n+2}.
\]

## 4. Почему нужен low-`u`

При `u=2.5` соседние beta-two parent modes порождают beta-four sector с фиксированным положительным action defect. Polynomial-small interaction coefficient не может подавить такой экспоненциальный выигрыш.

При

\[
\boxed{u=1.8}
\]

beta-three и beta-four уже не имеют growing turning branches на выбранном source interval, а beta-one и beta-two сохраняют нужную relay-структуру.

Берём

\[
\boxed{x=0.70}
\]

и центральный core

\[
|z-x|\le0.03,
\]

лежащий внутри Gaussian-supported strip

\[
2/3\le z\le4/3.
\]

## 5. Boundary-layer scaling

Выбирается

\[
\boxed{\delta_S=\kappa/S.}
\]

На stretched clock

\[
\tau=St
\]

одна ячейка остаётся длины порядка единицы. Orbit slope spacing становится `O(S^{-1})`, а число source-supported characters — `O(S)`.

Limiting orbit equations:

\[
\partial_\tau c=a_C Rc,
\qquad
\partial_\tau q=a_P Rq.
\]

При

\[
\lambda_C=2\kappa a_C,
\qquad
\mu_P=2\kappa a_P
\]

получаем

\[
\boxed{\mathcal P_C=R^{-1}e^{\lambda_CR},}
\]

\[
\boxed{\mathcal P_P=R^{-2}e^{\mu_PR}.}
\]

## 6. Limiting bilateral profiles

Для shift eigenprofiles

\[
Rc=\rho_Cc,
\qquad
Rq=\rho_Pq
\]

fixed equations равны

\[
\boxed{\frac{e^{\lambda_C\rho_C}}{\rho_C}=1,}
\]

\[
\boxed{\frac{e^{\mu_P\rho_P}}{\rho_P^2}=1.}
\]

В рабочей точке:

\[
\boxed{\rho_C=0.3510126502440001\ldots,}
\]

\[
\boxed{\rho_P=-2.147691668824314+1.235899139340218\,i,}
\]

\[
\boxed{\lambda_C=-2.982607649202283\ldots,}
\]

\[
\boxed{\mu_P=-0.845013757547658\ldots.}
\]

Также

\[
\boxed{\kappa_*=0.894049167184884\ldots,}
\qquad
\boxed{\theta_*=2.619416765747896\ldots.}
\]

Macroscopic dispersion equations transverse: catalyst scalar derivative и parent real `2x2` Jacobian ненулевые.

## 7. Совместимость одного root

Один и тот же beta-zero root должен реализовать сдвиг и catalyst-, и parent-сектора. Это достигается не двумя независимыми amplitudes, а одной amplitude плюс transverse polarization parameter.

В source positive-coordinate normalization sector-dependent hidden scalar отсутствует. Нужный ratio реализуется при

\[
\boxed{\tau_*=-0.2087411867089201\ldots.}
\]

Это закрывает principal single-root compatibility.

## 8. Finite-`S` tangent-Gaussian normal form

Физически существенная масса сосредоточена при

\[
|j|=O(\sqrt S).
\]

Положим

\[
h_S=S^{-1/2},
\qquad
y=jh_S.
\]

После выделения geometric factor finite-`S` map имеет вид

\[
\boxed{
\mathcal P_{b,S}^{tan}
=I+h_S(v_b\partial_y+B_by+C_b)+O(h_S^2).
}
\]

Численно

\[
\boxed{v_C=-2.046933015584520\ldots,}
\]

\[
\boxed{v_P=-0.185170992872966-1.044351775683794\,i,}
\]

\[
\boxed{B_C=1.509777659068068\ldots,}
\]

\[
\boxed{B_P=-4.618831967884313+2.657928294237038\,i.}
\]

Leading profile equation:

\[
\boxed{v_bf_b'(y)+(B_by+C_b)f_b(y)=0.}
\]

Её решения являются Gaussian/shifted-Gaussian profiles.

## 9. Physical localization

Для physical action weight

\[
H_b'(z)=u(\Gamma_b(z)-\Gamma_b(x)).
\]

В центре:

\[
H_1''(x)=-1.915959376503904\ldots,
\]

\[
H_2''(x)=-4.721509426848687\ldots.
\]

Хотя coefficient normal form имеет умеренный anti-Gaussian drift, physical action Gaussian сильнее. Условие

\[
\Re(B_b/v_b)>-2\alpha_bd_b^2
\]

выполняется в обоих секторах с заметным запасом.

Следовательно центральный tangent-Gaussian profile физически допустим.

## 10. Mean root и residual PDE correction

Beta-zero root имеет source order `M_{1/2}` и реализуется exact divergence-free Cauchy/curl construction.

Его principal self-advection равно нулю из-за ортогональности polarization к phase normal. В phase-adapted normalized norm:

- whole-space Leray имеет norm 1;
- root transport является bounded first-order coefficient;
- root multiplication даёт только fixed lattice shift;
- coupled residual mean/nonzero fixed point является contraction после подходящего weighting двух компонентов.

Это позволяет решать exact zero-residual correction вокруг заданного principal state. Но это не означает exact reset всех designated orbit coordinates.

## 11. Compact-support obstruction

При каждом finite `S` primary bank конечен по orbit index.

Пусть `c` — ненулевой finitely supported catalyst vector и `j_0` — его левый край. Тогда

\[
(e^{\lambda_CR}c)_{j_0}=c_{j_0}\ne0,
\]

но

\[
(Rc)_{j_0}=0.
\]

Значит

\[
\boxed{\ker_{c_{00}}(e^{\lambda_CR}-R)=\{0\}.}
\]

Аналогично

\[
\boxed{\ker_{c_{00}}(e^{\mu_PR}-R^2)=\{0\}.}
\]

Следовательно exact reset state не может состоять только из compact primary bank.

## 12. Corrected local target

Нужно искать

\[
\boxed{U_S=U_{core,S}+z_{tail,S}}
\]

с

- `U_core,S` — source-supported tangent-Gaussian primary profile;
- `z_tail,S` — элемент completed analytic correction lattice.

Boundary defect имеет размер

\[
\|d_{bd,S}\|\le S^Ae^{-cS}.
\]

То есть размер tail совместим с имеющимся correction budget.

## 13. Instability центрального bilateral space

Canonical bilateral profile не является transversely attracting. В catalyst sector spectral multiplier

\[
m_C(\zeta)=\frac{e^{\lambda_C\zeta}}{\zeta}
\]

имеет expanding directions; максимальный one-cell expansion по natural spectral circle превышает 8.

Parent sector также имеет stable и unstable directions.

Следовательно одного summable dyadic mismatch недостаточно для infinite cascade theorem.

## 14. Analytic-tail spectral separation

Для tail norm при

\[
\boxed{\sigma_0=0.005}
\]

shift spectrum лежит в annulus

\[
\boxed{e^{-3\sigma_0}\le|\zeta|\le e^{3\sigma_0}}
\]

то есть примерно

\[
0.98511\le|\zeta|\le1.01512.
\]

Catalyst symbol

\[
F_C(\zeta)=1-\frac{e^{\lambda_C\zeta}}{\zeta}
\]

и parent symbol

\[
F_P(\zeta)=1-\frac{e^{\mu_P\zeta}}{\zeta^2}
\]

не имеют нулей в этом annulus.

По weighted Wiener lemma:

\[
\boxed{(I-\mathcal P_C)^{-1}:\mathcal A_{\sigma_0}\to\mathcal A_{\sigma_0}}
\]

и

\[
\boxed{(I-\mathcal P_P)^{-1}:\mathcal A_{\sigma_0}\to\mathcal A_{\sigma_0}}
\]

ограничены.

Тем самым центральная rough-spectrum instability и analytic-tail invertibility действительно разделяются.

## 15. Открытый finite-`S` theorem

Следующий локальный theorem должен доказать

\[
\boxed{
\mathcal P_S(U_{core,S}+z_{tail,S})
=U_{core,S}+z_{tail,S}.
}
\]

Нужно показать, что после отделения tangent-Gaussian core exact finite-`S` tail operator является достаточно малым perturbation обратимого limiting tail operator, либо доказать эквивалентную block-Volterra схему около boundary layer.

До этого exact full-state finite-`S` reset не заявляется.

## 16. Inter-cell problem

Dyadic resampling tangent-Gaussian profile имеет summable error, но central bilateral spectrum содержит expanding directions. Поэтому для global assembly требуется:

1. exact scale-dependent invariant profile;
2. nonautonomous stable/center manifold, совместимый с Cauchy constraints;
3. или единая forward sequence-space dynamics, автоматически порождающая нужные tails.

## 17. Заключение

Low-`u` boundary-layer analysis заменяет future-time controls на реальный beta-zero Cauchy root, выделяет физически локализованный tangent-Gaussian core и одновременно показывает невозможность exact compact-bank reset.

Корректный объект — core+analytic-tail state. Предельный tail operator уже обратим, поэтому оставшийся локальный барьер — finite-`S` variable-coefficient Lyapunov–Schmidt completion, а не limiting spectral obstruction.

## Благодарности и вычислительная поддержка

В исследовательском процессе широко использовались AI-assisted symbolic calculations, code search, source comparison, numerical exploration и proof auditing. В статью включены только утверждения, поддерживаемые зафиксированным theorem chain и явно указанными вычислениями.

## Литература

1. OpenAI, *Finite time blowup for Navier–Stokes*, 2026. Lean source: `openai/NavierStokesAndEuler`, snapshot `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.
2. OpenAI, source files `PhysicalResidualBridge.lean`, `CommonBaseContext.lean`, `WeightedClasses.lean`, `LabelSumBounds.lean`, `PrimaryPulseBounds.lean`, `PhysicalMeanJetBounds.lean`.
3. Малачевский А.А., *Когда 10 000 ИИ-математиков пошли на Навье–Стокса*, Zenodo, DOI 10.5281/zenodo.22673644, 2026. Фоновая программная публикация; не используется как основание математических утверждений настоящей статьи.

## Reproducibility snapshot

Основной publication snapshot:

`9add88598582959095c418a252a5d0d13ed9596f`

Дополнительный limiting-tail theorem:

`4451d359a4e9d9b114476808ca6cb2d6bd744bde`.

Численные десятичные margins перед архивной публикацией должны быть подтверждены interval/outward-rounded audit.
