import ROOT as rt
from ROOT import TH1D,TH2D,TFile,TTree,TCanvas
import os, sys
import math
from math import sin, cos, sqrt

import argparse
import re
import optparse

parser = argparse.ArgumentParser(description='baseline selection')
parser.add_argument('-f', dest='infile', default='', help='local file input')
parser.add_argument('-y', dest='year', default='2016', help='year of dataset')
args = parser.parse_args()

print "year: ", args.year
print "dataset_name: ", args.infile

year = args.year
#fFile = TFile(args.infile, "READ")
fFile = TFile.Open(args.infile)
fTree = fFile.Get("Events")

#fFile1 = TFile("test.root", "recreate")

fCanvas = TCanvas("c", "c", 800, 800)
fHist1p = TH2D("btag_passwp_b_"+year, "", 50, 0, 1500, 50, -2.5, 2.5)
fHist2p = TH2D("btag_passwp_c_"+year, "", 50, 0, 1500, 50, -2.5, 2.5)
fHist3p = TH2D("btag_passwp_light_"+year, "", 50, 0, 1500, 50, -2.5, 2.5)

fHist1 = TH2D("btag_b_"+year, "", 50, 0, 1500, 50, -2.5, 2.5)
fHist2 = TH2D("btag_c_"+year, "", 50, 0, 1500, 50, -2.5, 2.5)
fHist3 = TH2D("btag_light_"+year, "", 50, 0, 1500, 50, -2.5, 2.5)
nEntries = fTree.GetEntries()
for i in range(0, nEntries):
    fTree.GetEntry(i)
    for j in range (0,fTree.nJet):
    	#if fTree.fHist.Fill(fTree.var1, fTree.var2)
        if year == "2018":
            if fTree.Jet_hadronFlavour[j] == 5:
               fHist1.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2783:
                  fHist1p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 4:
               fHist2.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2783:
                  fHist2p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 0:
               fHist3.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2783:
                  fHist3p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
        if year == "2017":
            if fTree.Jet_hadronFlavour[j] == 5:
               fHist1.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.3040:
                  fHist1p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 4:
               fHist2.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.3040:
                  fHist2p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 0:
               fHist3.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.3040:
                  fHist3p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])

        if year == "2016post":
            if fTree.Jet_hadronFlavour[j] == 5:
               fHist1.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2489:
                  fHist1p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 4:
               fHist2.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2489:
                  fHist2p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 0:
               fHist3.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2489:
                  fHist3p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])


        if year == "2016pre":
            if fTree.Jet_hadronFlavour[j] == 5:
               fHist1.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2598:
                  fHist1p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 4:
               fHist2.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2598:
                  fHist2p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])
            if fTree.Jet_hadronFlavour[j] == 0:
               fHist3.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j]) 
               if fTree.Jet_btagDeepFlavB[j] >0.2598:
                  fHist3p.Fill(fTree.Jet_pt[j], fTree.Jet_eta[j])


fFile1 = TFile("test.root", "recreate")
fHist1.Write()
fHist2.Write()
fHist3.Write()
fHist1p.Write()
fHist2p.Write()
fHist3p.Write()

fFile.Close()
fFile1.Close()

