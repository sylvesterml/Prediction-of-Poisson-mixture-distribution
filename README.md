# Prediction of Poisson mixture distribution  
## 何をしているのか？  
あるポアソン混合分布から得られたサンプルデータを元にギブスサンプリング（Gibbs Sampling）または変分推論（Variational Inference）を用いて元のポアソン混合分布を導出しています．
詳細は以下の本の4章にあるので，興味のある方はそちらを参照してください．  
[ベイズ推論による機械学習入門](https://www.kspub.co.jp/book/detail/1538320.html)  

## 具体的にはどのようなタスクか？  
タスク：「ある混合ポアソン分布からサンプリングされたデータを元に元の混合ポアソン分布を導出した」  
解決策：「ギブスサンプリングまたは変分推論を用いてサンプリングされたデータから混合ポアソン分布の母数を導出する」  
まず，以下のような混合ポアソン分布が存在するとします．  
![original_poisson](https://github.com/sylvesterml/Prediction-of-Poisson-mixture-distribution/blob/master/pictures/Original_Poisson.png)  
  
次に，この混合ポアソン分布から100点のみサンプリングする．
サンプリングした100点は以下のようになる．
![sampling_data](https://github.com/sylvesterml/Prediction-of-Poisson-mixture-distribution/blob/master/pictures/Sampling_Poisson.png)  
  
このように得られたサンプリングデータから元の混合ポアソン分布を導出する．  
まず用いるのはギブスサンプリングである．
ギブスサンプリングによって推定した元の混合ポアソン分布は以下のようになる．  
![gibbs_sapmling](https://github.com/sylvesterml/Prediction-of-Poisson-mixture-distribution/blob/master/pictures/Gibbs_Sampling_Poisson.png)  

次に用いるのは変分推論である．
変分推論によって推定した元の混合ポアソン分布は以下のようになる．  
![variational_inference](https://github.com/sylvesterml/Prediction-of-Poisson-mixture-distribution/blob/master/pictures/Variational_Inference_Poisson.png)  

## テストデータについて  
test.pyは以下の条件で実行する．  
