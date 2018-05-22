 Найдите **ошибку** нейрона с номером $j$ из выходного слоя. Тип нейрона — сигмоидальный.

$$ J=\frac{1}{2}∑_{j=1}^K(\hat{y_j}−y_j)^2 $$

или 

$$  \delta^L_j=\frac{1}{2}∑_{j=1}^K(\sigma(z_j)−y_j)^2 $$

Найдем следующую производную

$$ \frac{\delta J}{\delta z_j^L} = (\sigma(z_j)−y_j)* \sigma(z_j)*(1-\sigma(z_j)) = (\sigma(z_j)−y_j) * (\sigma(z_j)- \sigma(z_j)^2)$$